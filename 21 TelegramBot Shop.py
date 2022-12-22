import telebot
import os.path

config = {
    "name": "HappyRSPBot",
    "token": "5981874060:AAGgIW_t1oiUMuVZSJQLSpWKE3l7MzOqk4o"
}

happy_rsp = telebot.TeleBot(config["token"])

goods = {}
shopping = []
my_list = []
my_id = []

path1 = os.path.join("", "text1.txt")
file1 = open(path1, "r")
for my_line in file1.readlines():
    element = my_line.split(" - ")
    x = element[1].rstrip()
    goods[element[0]] = x
file1.close()

@happy_rsp.message_handler(content_types=['text'])
def get_text(message):
    inlines = telebot.types.InlineKeyboardMarkup()
    happy_rsp.send_message(message.chat.id, "Hello!")
    inlines.add(telebot.types.InlineKeyboardButton(text='Buy', callback_data="Buy"))
    inlines.add(telebot.types.InlineKeyboardButton(text='No', callback_data="No"))
    happy_rsp.send_message(message.chat.id, "Do you want to buy something?", reply_markup=inlines)

@happy_rsp.callback_query_handler(func=lambda call: call.data in ['Buy', 'No'])
def step1(call):
    if call.data == "Buy":
        inlines1 = telebot.types.InlineKeyboardMarkup()
        inlines1.add(telebot.types.InlineKeyboardButton(text='Shampoo', callback_data="Shampoo"))
        inlines1.add(telebot.types.InlineKeyboardButton(text='Balsams', callback_data="Balsams"))
        happy_rsp.send_message(call.message.chat.id, "Choose a category", reply_markup=inlines1)
    else:
        happy_rsp.send_message(call.message.chat.id, "Your choice: ")
        path2 = os.path.join("", "text2.txt")
        file2 = open(path2, "r")
        myid = str(call.from_user.id)
        print(myid)
        my_list = file2.readlines()
        for element3 in my_list:
            if element3.startswith(myid):
                element3.split(" - ")
                my_id.append(element3[1])
        file2.close()
        if len(my_id) > 0:
            happy_rsp.send_message(call.message.chat.id, '\n'.join(my_id))
            path3 = os.path.join('', myid + ".txt")
            file3 = open(path3, "w")
            for element4 in my_id:
                file3.write(element4 + '\n')
            file3.close()
            my_id.clear()
        else:
            happy_rsp.send_message(call.message.chat.id, "Nothing. You wasted my time!")


@happy_rsp.callback_query_handler(func=lambda call: call.data in ['Shampoo', 'Balsams'])
def step2(call):
    if call.data == 'Shampoo':
        for element in goods:
            index = goods[element]
            if index == 'Shampoo':
                shopping.append(element)
    elif call.data == 'Balsams':
        for element in goods:
            index = goods[element]
            if index == 'Balsams':
                shopping.append(element)
    inlines2 = telebot.types.InlineKeyboardMarkup()
    for elem in shopping:
        inlines2.add(telebot.types.InlineKeyboardButton(text=elem, callback_data=elem))
    happy_rsp.send_message(call.message.chat.id, 'Choose your item', reply_markup=inlines2)

@happy_rsp.callback_query_handler(func=lambda call: call.data in [*shopping])
def step3(call):
    path2 = os.path.join("", "text2.txt")
    file2 = open(path2, "a")
    myid = call.from_user.id
    user_id = str(myid)
    for element1 in shopping:
        if call.data == element1:
            file2.write(user_id)
            file2.write(" - " + element1 + "\n")
    shopping.clear()
    file2.close()
    inlines3 = telebot.types.InlineKeyboardMarkup()
    inlines3.add(telebot.types.InlineKeyboardButton(text='Buy', callback_data="Buy"))
    inlines3.add(telebot.types.InlineKeyboardButton(text='No', callback_data="No"))
    happy_rsp.send_message(call.message.chat.id, "Do you want to continue shopping?", reply_markup=inlines3)

happy_rsp.polling(none_stop=True, interval=0)