import telebot

config = {
    "name": "HappyRSPBot",
    "token": "5981874060:AAGgIW_t1oiUMuVZSJQLSpWKE3l7MzOqk4o"
}

happy_rsp = telebot.TeleBot(config["token"])

@happy_rsp.message_handler(content_types=["text"])
def get_text(message):
    if message.text == "Hello":
        happy_rsp.send_message(message.chat.id, f"Hello, user! What do you want to count?")
    else:
        happy_rsp.send_message(message.chat.id, "I'm glad to see you")
    happy_rsp.send_message(message.chat.id, "What do you want to count?")
    happy_rsp.register_next_step_handler(message, palindrom)

def palindrom(message):
    try:
        a = message.text                    #заганяю повідомлення від користувача в список
        s = list(a)
        q = []
        r = []
        b = ''
        f = "1234567890"
        result5 = 0
        for element in s:                   #розбиваю список на цифри та символи арифметичних дій
            if element.isdigit():
                b = b + element
            else:
                if b != "":
                    q.append(b)
                q.append(element)
                b = ""

        for y in range(len(a) - 1, -1, -1):
            if s[y] in f:
                r.append(s[y])
            else:
                break

        for elem in q:
            if elem == " " or elem == '':
                x = q.index(elem)
                del q[x]
            else:
                continue

        r.reverse()
        for e in r:
            b.join(e)
        q.append(b)

        for element in q:                                   #по черзі роблю всі арифметичні дії, редагую списки
            if element == "*":
                if len(q) == 3:
                    result5 = float(q[0]) * float(q[2])
                    break
                else:
                    i = q.index(element)
                    e1 = float(q[i - 1])
                    e2 = float(q[i + 1])
                    result1 = e1 * e2
                    q.insert(i - 1, result1)
                    i1 = q.index(result1)
                    del q[i1 + 1]
                    del q[i1 + 1]
                    del q[i1 + 1]

        for element in q:
            if element == "/":
                if len(q) == 3:
                    result5 = float(q[0]) / float(q[2])
                    break
                else:
                    i = q.index(element)
                    e1 = float(q[i - 1])
                    e2 = float(q[i + 1])
                    result2 = e1 / e2
                    q.insert(i - 1, result2)
                    i2 = q.index(result2)
                    del q[i2 + 1]
                    del q[i2 + 1]
                    del q[i2 + 1]

        for element in q:
            if element == "+":
                if len(q) == 3:
                    result5 = float(q[0]) + float(q[2])
                    break
                else:
                    i = q.index(element)
                    e1 = float(q[i - 1])
                    e2 = float(q[i + 1])
                    if q[i - 2] == "+":
                        result3 = e1 + e2
                    else:
                        result3 = e1 - e2
                    q.insert(i - 1, result3)
                    i3 = q.index(result3)
                    del q[i3 + 1]
                    del q[i3 + 1]
                    del q[i3 + 1]

        for element in q:
            if element == "-":
                if len(q) == 3:
                    result5 = float(q[0]) - float(q[2])
                    break
                else:
                    while len(q) > 3:
                        i = q.index(element)
                        e1 = q[i - 1]
                        e2 = q[i + 1]
                        result4 = e1 - e2
                        q.insert(i - 1, result4)
                        i4 = q.index(result4)
                        del q[i4 + 1]
                        del q[i4 + 1]
                        del q[i4 + 1]
                result5 = q[0] - q[2]

        happy_rsp.send_message(message.chat.id, f"Your result is: {round(result5, 2)}")
        happy_rsp.send_message(message.chat.id, 'Do you want to continue?')
        happy_rsp.register_next_step_handler(message, count_again)
    except:
        happy_rsp.send_message(message.chat.id, "Somethig's wrong. See you next time")

def count_again(message):
    work = message.text
    if work.lower() == "yes":
        happy_rsp.send_message(message.chat.id, 'What do you want to count?')
        happy_rsp.register_next_step_handler(message, palindrom)
    else:
        happy_rsp.send_message(message.chat.id, 'See you again')

happy_rsp.polling(none_stop=True, interval=0)