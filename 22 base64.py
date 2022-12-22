import telebot
import base64

config = {
    "name": "HappyRSPBot",
    "token": "5981874060:AAGgIW_t1oiUMuVZSJQLSpWKE3l7MzOqk4o"
}

happy_rsp = telebot.TeleBot(config["token"])

@happy_rsp.message_handler(content_types=['text'])
def get_text(message):
    happy_rsp.send_message(message.chat.id, "Hello! Will you show me anything?")

@happy_rsp.message_handler(content_types=['photo'])
def download_image(message):
    fileID = message.photo[-1].file_id
    file_info = happy_rsp.get_file(fileID)
    downloaded_file = happy_rsp.download_file(file_info.file_path)

    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    encode = base64.b64decode(downloaded_file)
    happy_rsp.reply_to(message, str(encode))

happy_rsp.polling(none_stop=True, interval=0)