import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('hi.webm', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #клава біля клави
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("09.02")
    item2 = types.KeyboardButton("16.02")
    item3 = types.KeyboardButton("23.02")
    item4 = types.KeyboardButton("02.03")
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Які ж сьогодні _страждання_ чекають на тебе?".format(message.from_user, bot.get_me()), parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(commands=['monday'])
def monday(message):
    bot.send_message(message.chat.id,
                     "*4. 13:30-14:50*\n_Іноземна мова - 043а_\n*5. 15:05-16:25*\n_Функ.аналіз(лаб) - 147_\n*6. 16:40 - 18:00*\n_ФтДП - Черемшини,31 (поч.17:15)_".format(
                         message.from_user, bot.get_me()), parse_mode="Markdown")


@bot.message_handler(commands=['tuesday'])
def tuesday(message):
    bot.send_message(message.chat.id, "*1. 8:30-9:50*\n_Р-ня мат.фізики(лекція) - 266_\n*2. 10:10-11:30*\n_Програм.забез.(лаб) - 118а_\n*3. 11:50-13:10*\n_Дввс_\n*4. 13:30-14:50*\n_Дввс_\n".format(message.from_user, bot.get_me()), parse_mode="Markdown")


@bot.message_handler(commands=['wednesday'])
def wednesday(message):
    bot.send_message(message.chat.id, "*1. 8:30-9:50*\n_Чис.мет.лін.алг(лаб) - 261_\n*2. 10:10-11:30*\n_Р-ння мат.фізики(практ) - 366_\n*3. 11:50-13:10*\n_Функ.аналіз(лекція) - 111_\n*4. 13:30-14:50*\n_Іноземна мова - 043а_\n".format(message.from_user, bot.get_me()), parse_mode="Markdown")


@bot.message_handler(commands=['thursday'])
def thursday(message):
    bot.send_message(message.chat.id, "*1. 8:30-9:50*\n_ТІМС(лекція) - 266_\n*2. 10:10-11:30*\n_Програм.забезп.(лекція) - 146_\n*3. 11:50-13:10*\n_Числ.мет.лін.алг(лекція) - 111_\n".format(message.from_user, bot.get_me()), parse_mode="Markdown")


@bot.message_handler(commands=['friday'])
def friday(message):
    bot.send_message(message.chat.id, "*1. 8:30-9:50*\n_ТІМС(лаб) - 366_\n*2. 10:10-11:30*\n_Навчальна практ(лаб) - 118а_\n*3. 11:50-13:10*\n_Дввс_\n*4. 13:30-14:50*\n_Дввс_\n".format(message.from_user, bot.get_me()), parse_mode="Markdown")


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '09.02':
            bot.send_message(message.chat.id,
                             "*4. 13:30-14:50*\n_Іноземна мова - 043а_\n*5. 15:05-16:25*\n_Функ.аналіз(лаб) - 147_\n*6. 16:40 - 18:00*\n_ФтДП - 41(д)_".format(
                                 message.from_user, bot.get_me()), parse_mode="Markdown")
        elif message.text == '16.02':
            bot.send_message(message.chat.id,
                             "*4. 13:30-14:50*\n_Іноземна мова - 043а_\n*5. 15:05-16:25*\n_Функ.аналіз(лаб) - 147_\n*6. 16:40 - 18:00*\n_ФтДП - 303(с)_".format(
                                 message.from_user, bot.get_me()), parse_mode="Markdown")
        elif message.text == '02.03':
            bot.send_message(message.chat.id,
                             "*4. 13:30-14:50*\n_Іноземна мова - 043а_\n*5. 15:05-16:25*\n_Функ.аналіз(лаб) - 147_\n*6. 16:40 - 18:00*\n_ФтДП - 303(с)_".format(
                                 message.from_user, bot.get_me()), parse_mode="Markdown")
        elif message.text == '23.02':
            bot.send_message(message.chat.id,
                             "*4. 13:30-14:50*\n_Іноземна мова - 043а_\n*5. 15:05-16:25*\n_Функ.аналіз(лаб) - 147_\n*6. 16:40 - 18:00*\n_ФтДП - 41(д)_".format(
                                 message.from_user, bot.get_me()), parse_mode="Markdown")

bot.polling(none_stop=True)
