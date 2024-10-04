import telebot
import wikipedia
import re


bot = telebot.TeleBot("7040632379:AAG1EP9Fqe4qYngl7DVE_p3NrjD3jxaTKPA")

wikipedia.set_lang('ru')

def gewiki(s):
    try:
        ny = wikipedia.page(s)
        witext = ny.content[:10000]
        wimas = witext.split('.')
        witext2 =''

        for i in wimas:
            if not('==' in i):
                if(len((i.strip())) > 3):
                    witext2 = witext2 + i
            else:
                break
        witext2 = re.sub(r'\([^()]*\)', '', witext2)
        witext2 = re.sub(r'\[[^\]]*\]', '', witext2)
        witext2 = re.sub(r'\{[^\}]*\}', '', witext2)
        return witext2
    except Exception as e:
        return 'Нет такой инфы'



@bot.message_handler(commands= ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Отправь мне слово, и я найду его')

# что отправляет пользователь 
@bot.message_handler(content_types =['text'])
def handle_text(message):
    bot.send_message(message.chat.id, gewiki(message.text))

bot.polling(non_stop = True, interval = 0)





# @bot.message_handler(commands= ['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Напиши мне что-то')

# # что отправляет пользователь 
# @bot.message_handler(content_types =['text'])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Ты написал ' + message.text)

# bot.polling(non_stop = True, interval = 0)