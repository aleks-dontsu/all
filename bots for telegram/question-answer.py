import telebot
from telebot import types

# OptimizerSEObot
bot = telebot.TeleBot('************************************************')

menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
menu.add(
    types.KeyboardButton('Записаться на курс'), types.KeyboardButton('Расписание занятий'),
    types.KeyboardButton('Контакты'), types.KeyboardButton('Сайт')
)


SEO_optimization = 'СЕО оптимизация - текст, текст, текст, текст, текст, текст, текст, текст, текст, текст, '
create_site = 'Создание сайтов - текст, текст, текст, текст, текст, текст, текст, текст, текст, текст, '
context = 'Контекстная реклама - текст, текст, текст, текст, текст, текст, текст, текст, текст, текст, '


def kb(message):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    button_1 = types.InlineKeyboardButton(text='СЕО оптимизация', callback_data='call_1')
    button_2 = types.InlineKeyboardButton(text='Создание сайтов', callback_data='call_2')
    button_3 = types.InlineKeyboardButton(text='Контекстная реклама', callback_data='call_3')
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, "Выбери курс:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "call_1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=SEO_optimization)
    elif call.data == "call_2":
        bot.answer_callback_query(call.id, text=create_site)
    elif call.data == "call_3":
        bot.send_message(chat_id=call.message.chat.id, text=context)
    else:
        pass


@bot.message_handler(commands=['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Наш сайт', url='https://webinar.optimizer-seo.com/')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы получить ответ на интересующийся вопрос " \
                   f"просто напиши его или выбери из меню популярных вопросов"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=menu)


blacklist = ['бля', 'хуй', 'пизд', 'пидар', 'сука', 'суки']


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    for x in blacklist:
        if x in get_message_bot:
            bot.delete_message(message.chat.id, message.message_id)

    if get_message_bot == "записаться на курс":
        kb(message)
    elif get_message_bot == "расписание занятий":
        bot.send_message(message.chat.id, 'Расписание занятий:\nПн: с 19:00 до 21:00\nСр: с 19:00 до 21:00',
                         parse_mode='html')
    elif get_message_bot == "контакты":
        bot.send_message(message.chat.id, f'Наши контакты\n063-123-45-67\n068-123-45-67', parse_mode='html')
    elif get_message_bot == "сайт":
        url(message)
    elif get_message_bot == "привет":
        final_message = f'Привет\nКак дела??'
    elif get_message_bot == "норм":
        final_message = f'У меня так-же..\nчто делаешь??'
    else:
        final_message = f'Личные вопросы Вы можете задать по телефону: \n+38(063)123-45-67'

    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
