import telebot
import webbrowser

bot = telebot.TeleBot('7421094099:AAEsopBl5a5zF0CrqKG1n7KRAMyR6x_Z2yM')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.google.com')



@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет меня зовут, {message.from_user.first_name} ' )



# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, '<b>Hello</b> <em><u>information</u></em>', parse_mode='html')



# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, f'Привет меня зовут, {message.from_user.first_name} ' )
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')
    




bot.polling(none_stop=True)