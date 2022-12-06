import telebot
import os.path

config = {
    "name": "HappyRSPBot",
    "token": "5981874060:AAGgIW_t1oiUMuVZSJQLSpWKE3l7MzOqk4o"
}

happy_rsp = telebot.TeleBot(config["token"])

path = os.path.join("", "text1.txt")

@happy_rsp.message_handler(content_types=["text"])
def get_text(message):
    if message.text == "Hello":
        happy_rsp.send_message(message.chat.id, f"Hello, user!")
    else:
        happy_rsp.send_message(message.chat.id, "I'm glad to see you")
    happy_rsp.send_message(message.chat.id, "How do you call yourself?")
    happy_rsp.register_next_step_handler(message, palindrom)

def palindrom(message):                                                 # реєстрація логін
    login = message.text
    myfile = open(path, 'a')
    myfile.write(login)
    myfile.write("\n")
    myfile.close()
    happy_rsp.send_message(message.chat.id, "What's your password?")
    happy_rsp.register_next_step_handler(message, passw)

def passw(message):                                                     # реєстрація гасло
    password = message.text
    myfile = open(path, 'a')
    myfile.write(password)
    myfile.write("\n")
    myfile.close()
    happy_rsp.send_message(message.chat.id, "Let's check! So, what's your login?")
    happy_rsp.register_next_step_handler(message, autorization)

def autorization(message):                                              # авторизація логін
    login = message.text
    myfile = open(path, 'r')
    check = myfile.readlines()
    check1 = check[0].rstrip("\n")
    if login == check1:
        happy_rsp.send_message(message.chat.id, "What's your password?")
        happy_rsp.register_next_step_handler(message, password)
    else:
        happy_rsp.send_message(message.chat.id, "I don't remember you. Let's start again. What's your name?")
        happy_rsp.register_next_step_handler(message, palindrom)
    myfile.close()


def password(message):                                                  # авторизація гасло
    passw = message.text
    myfile = open(path, 'r')
    passw2 = myfile.readlines()
    passw1 = passw2[1].rstrip("\n")
    if passw == passw1:
        happy_rsp.send_message(message.chat.id, "You're in")
    myfile.close()

happy_rsp.polling(none_stop=True, interval=0)