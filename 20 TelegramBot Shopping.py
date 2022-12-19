import telebot

config = {
    "name": "HappyRSPBot",
    "token": "5981874060:AAGgIW_t1oiUMuVZSJQLSpWKE3l7MzOqk4o"
}

happy_rsp = telebot.TeleBot(config["token"])

goods = {'Smoothing shampoo, 13 $': 'Shampoo', 'Nutrition shampoo, 11 $': 'Shampoo', 'Color protect shampoo, 11 $': 'Shampoo', 'Bonacure smoothing balsam, 15 $': 'Balsams',
         'Matrix color protect balsam, 13 $': 'Balsams', 'Invigo tonic balsam, 17 $': "Balsams"}
shopping = []
my_list = []



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
        if len(my_list) > 0:
            happy_rsp.send_message(call.message.chat.id, '\n'.join(my_list))
            my_list.clear()
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
    for element1 in shopping:
        if call.data == element1:
            my_list.append(element1)
    shopping.clear()
    inlines3 = telebot.types.InlineKeyboardMarkup()
    inlines3.add(telebot.types.InlineKeyboardButton(text='Buy', callback_data="Buy"))
    inlines3.add(telebot.types.InlineKeyboardButton(text='No', callback_data="No"))
    happy_rsp.send_message(call.message.chat.id, "Do you want to continue shopping?", reply_markup=inlines3)

happy_rsp.polling(none_stop=True, interval=0)