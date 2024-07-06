import telebot

bot = telebot.TeleBot('7251069411:AAHRYeZdLBwXzuNT0r1sAUlMvn8Mg4CKVeE')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!Я создал этого бота для теста! Если написать команду /gdesozdali, то там будет написано где он создан! Удачи в командах!')

@bot.message_handler(commands=['gdesozdali'])
def main(message):
    bot.send_message(message.chat.id, f'Он создан на Python! :3')
    bot.send_message(message.chat.id, f'Ок! это только начало! Фух, я уже долго пишу этот код! Ну, ладно! Напиши команду /iystalpisatkod. ОЙ нет не ту команду, или ту. {message.from_user.first_name}, помоги пожалуйста!')

@bot.message_handler(commands=['iystalpisatkod'])
def kvest(message):
    bot.send_message(message.chat.id, f'Я уссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссс...                      ОЙ!!! Произошла Ошибка! Код ошибки:488 Напишите этому пользователю @isaevivan926 за командой И ОБЯЗАТЕЛЬНО СКАЖИТЕ КОД ОШИБКИ!!!!!')

@bot.message_handler(commands=['helpboty'])
def kvest1(message):
    bot.send_message(message.chat.id, f'Операция выполняется! Пожалуйста подождите')
    bot.send_message(message.chat.id, f'Найдена ошибка в боте! Идет устранение ошибки! Пожалуйста подождите')
    bot.send_message(message.chat.id, f'Операция выполнена! Ура! Напиши команду /iystalpisatkоd просто нажми на нее! Удачи!')

@bot.message_handler(commands=['iystalpisatkоd'])
def kvest(message):
   bot.send_message(message.chat.id, f'!0_0! Ура спасибо что починил меня! А теперь напиши команду /hm чтобы я узнал о тебе больше!!!')  

@bot.message_handler(commands=['hm'])
def kvest(message):
   bot.send_message(message.chat.id, f'СПАСИБО')
   bot.send_message(message.chat.id, f'СПАСИБО ОГРОМНОЕ А ТЕПЕРЬ ННАПИШИ КОМАНДУ /IHACKYOU')

@bot.message_handler(commands=['IHACKYOU'])
def hack(message):
   bot.send_message(message.chat.id, f'Лилипуты')
   bot.send_message(message.chat.id, f'3 отряд')
   bot.send_message(message.chat.id, f'{message.from_user.first_name}')


bot.polling(none_stop=True)