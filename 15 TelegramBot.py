import telebot

config = {
    "name": "HappyRSPBot",
    "token": "5981874060:AAGgIW_t1oiUMuVZSJQLSpWKE3l7MzOqk4o"
}

happy_rsp = telebot.TeleBot(config["token"])

@happy_rsp.message_handler(content_types=["text"])
def get_text(message):
    if message.text == "Hello":
        happy_rsp.send_message(message.chat.id, f"Hello, user!")
    else:
        happy_rsp.send_message(message.chat.id, "I'm glad to see you")
    happy_rsp.send_message(message.chat.id, "Tell any word!")
    happy_rsp.register_next_step_handler(message, palindrom)


def palindrom(message):
    word = message.text
    word1 = word.lower()
    a = list(word1)
    b = len(a)/2
    if b % 2 == 0:
        list1 = a[:b]
        a.reverse()
        list2 = a[:b]
        part1 = "".join(list1)
        part2 = "".join(list2)
        if part1 == part2:
            happy_rsp.send_message(message.chat.id, "It's a palindrom")
        else:
            happy_rsp.send_message(message.chat.id, "It's not a palindrom")
    else:
        mynum = round(b)
        list1 = a[:mynum]
        a.reverse()
        list2 = a[:mynum]
        part1 = "".join(list1)
        part2 = "".join(list2)
        if part1 == part2:
            happy_rsp.send_message(message.chat.id, "It's a palindrom")
        else:
            happy_rsp.send_message(message.chat.id, "It's not a palindrom")
        happy_rsp.send_message(message.chat.id, "Tell any whole number!")
        happy_rsp.register_next_step_handler(message, evennumber)

def evennumber(message):
    num1 = message.text
    try:
        num2 = int(num1)
        if num2 % 2 == 0:
            happy_rsp.send_message(message.chat.id, "That's an EVEN number!")
        else:
            happy_rsp.send_message(message.chat.id, "That's an ODD number!")

    except:
        happy_rsp.send_message(message.chat.id, "That's not a whole number!")



happy_rsp.polling(none_stop=True, interval=0)
