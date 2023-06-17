import datetime
import calendar
import password

from aiogram import Dispatcher, Bot, executor, types
import bot_keyboard
from dbcommunicate import add_user, check_user_in_bd_by, add_point_for, show_all_res, delete_all_points_by


bot = Bot(password.TOKEN)
dp = Dispatcher(bot)


@dp.callback_query_handler(lambda cb: cb.data == 'question_zero_button_one')
async def process_order_tariff(callback_query: types.CallbackQuery):
    delete_all_points_by(callback_query.message.chat.id)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Для чого вам потрібен тариф?', reply_markup=bot_keyboard.question1)

#######

@dp.callback_query_handler(lambda cb: cb.data == 'question_one_button_one')
async def process_order_smartphone_gadget(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    add_point_for('free', chat_id, 2)
    add_point_for('smart', chat_id, 2)
    add_point_for('simple', chat_id, 2)
    add_point_for('platinum', chat_id, 2)
    add_point_for('school', chat_id, 2)
    add_point_for('gadjet', chat_id, 0)
    add_point_for('family', chat_id, 0)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Наскільки часто ви зазвичай розмовляєте по телефону?', reply_markup=bot_keyboard.inline_question_2)

###


@dp.callback_query_handler(lambda cb: cb.data == 'question_2second_button_one')
async def process_order_phone1_btn1(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    add_point_for('free', chat_id, 2)
    add_point_for('smart', chat_id, 1)
    add_point_for('simple', chat_id, 0)
    add_point_for('platinum', chat_id, 3)
    add_point_for('school', chat_id, 3)
    add_point_for('gadjet', chat_id, 0)
    add_point_for('family', chat_id, 0)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Скільки часу ви проводите в роумінгу або подорожуєте за кордоном??', reply_markup=bot_keyboard.question2)


@dp.callback_query_handler(lambda cb: cb.data == 'question_2second_button_two')
async def process_order_phone1_btn2(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    add_point_for('free', chat_id, 1)
    add_point_for('smart', chat_id, 2)
    add_point_for('simple', chat_id, 1.5)
    add_point_for('platinum', chat_id, 0)
    add_point_for('school', chat_id, 1)
    add_point_for('gadjet', chat_id, 0)
    add_point_for('family', chat_id, 0)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Скільки часу ви проводите в роумінгу або подорожуєте за кордоном??', reply_markup=bot_keyboard.inline_question_2)


@dp.callback_query_handler(lambda cb: cb.data == 'question_2second_button_three')
async def process_order_phone1_btn3(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    add_point_for('free', chat_id, 0)
    add_point_for('smart', chat_id, 0.5)
    add_point_for('simple', chat_id, 3)
    add_point_for('platinum', chat_id, 0)
    add_point_for('school', chat_id, 1)
    add_point_for('gadjet', chat_id, 0)
    add_point_for('family', chat_id, 0)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Скільки часу ви проводите в роумінгу або подорожуєте за кордоном??', reply_markup=bot_keyboard.inline_question_2)

###

@dp.callback_query_handler(lambda cb: cb.data == 'question_two_button_one')
async def process_order_phone2_btn1(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    add_point_for('free', chat_id, 2)
    add_point_for('smart', chat_id, 1)
    add_point_for('simple', chat_id, -1)
    add_point_for('platinum', chat_id, 3)
    add_point_for('school', chat_id, 2)
    add_point_for('gadjet', chat_id, 0)
    add_point_for('family', chat_id, 0)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Як часто ви використовуєте Інтернет і для яких цілей - перегляд відео, соціальні мережі, робота або інше?', reply_markup=bot_keyboard.question3)


@dp.callback_query_handler(lambda cb: cb.data == 'question_two_button_two')
async def process_order_phone2_btn2(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    add_point_for('free', chat_id, 2)
    add_point_for('smart', chat_id, 1)
    add_point_for('simple', chat_id, 0)
    add_point_for('platinum', chat_id, 2)
    add_point_for('school', chat_id, 2)
    add_point_for('gadjet', chat_id, 0)
    add_point_for('family', chat_id, 0)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Як часто ви використовуєте Інтернет і для яких цілей - перегляд відео, соціальні мережі, робота або інше?', reply_markup=bot_keyboard.question3)


@dp.callback_query_handler(lambda cb: cb.data == 'question_two_button_three')
async def process_order_phone2_btn3(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    add_point_for('free', chat_id, 0)
    add_point_for('smart', chat_id, 1)
    add_point_for('simple', chat_id, 2)
    add_point_for('platinum', chat_id, -1)
    add_point_for('school', chat_id, 1.5)
    add_point_for('gadjet', chat_id, 0)
    add_point_for('family', chat_id, 0)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Як часто ви використовуєте Інтернет і для яких цілей - перегляд відео, соціальні мережі, робота або інше?', reply_markup=bot_keyboard.question3)

###

@dp.callback_query_handler(lambda cb: cb.data == 'question_three_button_one')
async def process_order_phone3_btn1(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    add_point_for('free', chat_id, 3)
    add_point_for('smart', chat_id, 2)
    add_point_for('simple', chat_id, 0.5)
    add_point_for('platinum', chat_id, 3)
    add_point_for('school', chat_id, 1.5)
    add_point_for('gadjet', chat_id, 0)
    add_point_for('family', chat_id, 0)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Чи потрібна вам можливість безлімітних дзвінків на номери lifecell?', reply_markup=bot_keyboard.question4)


@dp.callback_query_handler(lambda cb: cb.data == 'question_three_button_two')
async def process_order_phone3_btn2(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    add_point_for('free', chat_id, 1.5)
    add_point_for('smart', chat_id, 2.5)
    add_point_for('simple', chat_id, 1)
    add_point_for('platinum', chat_id, 2)
    add_point_for('school', chat_id, 1)
    add_point_for('gadjet', chat_id, 0)
    add_point_for('family', chat_id, 0)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Чи потрібна вам можливість безлімітних дзвінків на номери lifecell?', reply_markup=bot_keyboard.question4)


@dp.callback_query_handler(lambda cb: cb.data == 'question_three_button_three')
async def process_order_phone3_btn3(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    add_point_for('free', chat_id, 0)
    add_point_for('smart', chat_id, 1)
    add_point_for('simple', chat_id, 2.5)
    add_point_for('platinum', chat_id, -1)
    add_point_for('school', chat_id, 1)
    add_point_for('gadjet', chat_id, 0)
    add_point_for('family', chat_id, 0)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Чи потрібна вам можливість безлімітних дзвінків на номери lifecell?', reply_markup=bot_keyboard.question4)


@dp.callback_query_handler(lambda cb: cb.data == 'question_three_button_four')
async def process_order_phone3_btn4(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    add_point_for('free', chat_id, -1.5)
    add_point_for('smart', chat_id, 0)
    add_point_for('simple', chat_id, 1)
    add_point_for('platinum', chat_id, -2)
    add_point_for('school', chat_id, 2)
    add_point_for('gadjet', chat_id, 0)
    add_point_for('family', chat_id, 0)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Чи потрібна вам можливість безлімітних дзвінків на номери lifecell?', reply_markup=bot_keyboard.question4)

###

@dp.callback_query_handler(lambda cb: cb.data == 'question_four_button_one')
async def process_order_phone4_btn1(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    add_point_for('free', chat_id, 2)
    add_point_for('smart', chat_id, 1)
    add_point_for('simple', chat_id, 0)
    add_point_for('platinum', chat_id, 2.5)
    add_point_for('school', chat_id, 3)
    add_point_for('gadjet', chat_id, 0)
    add_point_for('family', chat_id, 0)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, f'Дякую за вибір очікуйте результати... {show_all_res(callback_query.message.chat.id)}')


@dp.callback_query_handler(lambda cb: cb.data == 'question_four_button_two')
async def process_order_phone4_btn2(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    add_point_for('free', chat_id, 1.5)
    add_point_for('smart', chat_id, 1.5)
    add_point_for('simple', chat_id, 2)
    add_point_for('platinum', chat_id, -0.5)
    add_point_for('school', chat_id, 0.5)
    add_point_for('gadjet', chat_id, 0)
    add_point_for('family', chat_id, 0)
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, f'Дякую за вибір очікуйте результати... {show_all_res(callback_query.message.chat.id)}')

######

@dp.callback_query_handler(lambda cb: cb.data == 'question_one_button_two')
async def process_order_gadget(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Оберіть пристрій, який вам потрібен:\n'
                                                           '- /gadget_tablet - планшет\n'
                                                           '- /gadget_router - роутер\n'
                                                           '- /gadget_safety - сигналізація\n'
                                                           '- /gadget_smart - смарт-годинник\n')

######

@dp.callback_query_handler(lambda cb: cb.data == 'question_one_button_three')
async def process_order_family(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Ось тариф, який ідеально підійде вам\n'
                                                           '/family')

######
@dp.callback_query_handler(lambda cb: cb.data == 'question_one_button_two')
async def process_order_smartphone_gadget(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Ось список доступних вам пакетів:',
                           reply_markup=bot_keyboard.inline_question_2)


@dp.callback_query_handler(lambda cb: cb.data == 'question_one_button_three')
async def process_order_smartphone_gadget(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Ось список доступних вам пакетів:',
                           reply_markup=bot_keyboard.inline_question_2)


###

@dp.callback_query_handler(lambda cb: cb.data == 'question_one_button_three')
async def process_order_smartphone_gadget(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Ось список доступних вам пакетів:',
                           reply_markup=bot_keyboard.inline_question_2)

###

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not check_user_in_bd_by(message.chat.id):
        add_user(message.chat.id, message.chat.full_name)
    await bot.send_message(message.chat.id, 'Привіт користувач!\n\nЯкщо тобі потрібна допомога, просто поклич /help')
        

@dp.message_handler(commands=['order'])
async def order_tariff(message: types.Message):
    await bot.send_message(message.chat.id, 'Чи хочете ви підібрати оптимальний тариф?', reply_markup=bot_keyboard.question0)


selected_date = None
tariff_end_date = None


@dp.message_handler(commands=['calendar'])
async def show_calendar(message: types.Message):
    now = datetime.datetime.now()
    calendar_markup = generate_calendar_markup(now.year, now.month)
    await message.reply('calendar', reply_markup=calendar_markup)


def generate_calendar_markup(year, month):
    markup = types.InlineKeyboardMarkup(row_width=7)
    month_calendar = calendar.monthcalendar(year, month)

    for week in month_calendar:
        for day in week:
            if day != 0:
                callback_data = f"{year}-{month:02d}-{day:02d}"
                if selected_date and selected_date.day == day and selected_date.month == month and selected_date.year == year:
                    markup.insert(types.InlineKeyboardButton(f"[{day}]", callback_data=callback_data))
                else:
                    markup.insert(types.InlineKeyboardButton(str(day), callback_data=callback_data))

    today = datetime.date.today()
    if selected_date and selected_date == today:
        markup.insert(types.InlineKeyboardButton("[Поточна дата]", callback_data=today.isoformat()))
    else:
        markup.insert(types.InlineKeyboardButton("Поточна дата", callback_data=today.isoformat()))

    return markup


@dp.callback_query_handler(lambda c: c.data and datetime.datetime.strptime(c.data, "%Y-%m-%d"), state='*')
async def process_calendar_button(callback_query: types.CallbackQuery):
    global selected_date, tariff_end_date
    selected_date = datetime.datetime.strptime(callback_query.data, "%Y-%m-%d").date()
    tariff_end_date = selected_date + datetime.timedelta(days=28)
    response = f"Ви обрали дату: {selected_date.strftime('%d.%m.%Y')}\nТариф діятиме до: {tariff_end_date.strftime('%d.%m.%Y')}"
    await bot.send_message(callback_query.from_user.id, response)


@dp.message_handler(commands=['help'])
async def order_tariff(message: types.Message):
    await bot.send_message(message.chat.id, 'Ось весь список команд, які\n ти можеш використати\n\n'
                                            '/start - початок роботи\n'
                                            '/order - допомога при виборі тарифу\n'
                                            '/calendar - планування тарифу\n'
                                            '/free - Вільний Лайф\n'
                                            '/smart - Смарт Лайф\n'
                                            '/simple - Простий Лайф\n'
                                            '/platinum - Platinum Лайф\n'
                                            '/school - Шкільний Лайф\n'
                                            '/gadget_safety - Сайфіті Ґаджет\n'
                                            '/gadget_smart - Смарт Ґаджет\n'
                                            '/gadget_tablet - Смарт Планшет\n'
                                            '/gadget_router - Смарт Роутер')


# PAYING

@dp.message_handler(commands=['free'])
async def free(message: types.Message):
    text = "<b>Вільний Лайф!</b>\n\n" \
           "<b>180грн/4 тижні</b>\n\n"\
           "<b>В пакеті:</b>\n" \
           "   - Інтернет: Безлім\n" \
           "   - Дзвінки: 1600 хв" \
           "Більше інформації <a href='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/'>тут</a>"

    await message.reply(text, parse_mode=types.ParseMode.HTML)
    await bot.send_invoice(message.chat.id,
                           'Поповнення рахунку',
                           'Вільний Лайф',
                           'invoice',
                           password.PAYMENT_TOKE,
                           'UAH',
                           [types.LabeledPrice('Поповнення рахунку', 180 * 100)]
                           )


@dp.message_handler(commands=['smart'])
async def smart(message: types.Message):
    text = "<b>Смарт Лайф!</b>\n\n" \
           "<b>120грн/4 тижні</b>\n\n"\
           "<b>В пакеті:</b>\n" \
           "   - Інтернет: 25 ГБ\n" \
           "   - Дзвінки: 800 хв\n\n" \
           "Більше інформації <a href='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/'>тут</a>"

    await message.reply(text, parse_mode=types.ParseMode.HTML)
    await bot.send_invoice(message.chat.id,
                           'Поповнення рахунку',
                           'Смарт Лайф',
                           'invoice',
                           password.PAYMENT_TOKE,
                           'UAH',
                           [types.LabeledPrice('Поповнення рахунку', 120 * 100)]
                           )


@dp.message_handler(commands=['simple'])
async def simple(message: types.Message):
    text = "<b>Просто Лайф!</b>\n\n" \
           "<b>90грн/4 тижні</b>\n\n"\
           "<b>В пакеті:</b>\n" \
           "   - Інтернет: 8 ГБ\n" \
           "   - Дзвінки: 300 хв\n" \
           "Більше інформації <a href='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/'>тут</a>"

    await message.reply(text, parse_mode=types.ParseMode.HTML)
    await bot.send_invoice(message.chat.id,
                           'Поповнення рахунку',
                           'Просто Лайф',
                           'invoice',
                           password.PAYMENT_TOKE,
                           'UAH',
                           [types.LabeledPrice('Поповнення рахунку', 90 * 100)]
                           )


@dp.message_handler(commands=['school'])
async def simple(message: types.Message):
    text = "<b>Шкільний Лайф!</b>\n\n" \
           "<b>150грн/4 тижні</b>\n\n"\
           "<b>В пакеті:</b>\n" \
           "   - Інтернет: 7 ГБ\n" \
           "   - Дзвінки: Безліміт\n" \
           "Більше інформації <a href='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/'>тут</a>"

    await message.reply(text, parse_mode=types.ParseMode.HTML)
    await bot.send_invoice(message.chat.id,
                           'Поповнення рахунку',
                           'Шкільний Лайф',
                           'invoice',
                           password.PAYMENT_TOKE,
                           'UAH',
                           [types.LabeledPrice('Поповнення рахунку', 150 * 100)]
                           )


@dp.message_handler(commands=['platinum'])
async def platinum(message: types.Message):
    text = "<b>Platinum Лайф!</b>\n\n" \
           "<b>250грн/4 тижні</b>\n\n"\
           "<b>В пакеті:</b>\n" \
           "   - Інтернет: Безліміт\n" \
           "   - Дзвінки: 3000 хв" \

    await message.reply(text, parse_mode=types.ParseMode.HTML)
    await bot.send_invoice(message.chat.id,
                           'Поповнення рахунку',
                           'Вільний Лайф',
                           'invoice',
                           password.PAYMENT_TOKE,
                           'UAH',
                           [types.LabeledPrice('Поповнення рахунку', 250 * 100)]
                           )


@dp.message_handler(commands=['family'])
async def simple(message: types.Message):
    text = "<b>Смарт Сім'я</b>\n\n" \
           "<b>375 грн / 4 тижні</b>\n\n"\
           "<b>В пакеті:</b>\n" \
           "   - Інтернет: від 20 ГБ до 50 ГБ\n" \
           "   - Дзвінки: від 500 хв до 1500 хв\n" \
           "   - До 5 номерів\n" \
           "Більше інформації <a href='https://www.lifecell.ua/uk/mobilnij-zvyazok/smart-simya-series/'>тут</a>"

    await message.reply(text, parse_mode=types.ParseMode.HTML)
    await bot.send_invoice(message.chat.id,
                           'Поповнення рахунку',
                           'Сім`я',
                           'invoice',
                           password.PAYMENT_TOKE,
                           'UAH',
                           [types.LabeledPrice('Поповнення рахунку', 375 * 100)]
                           )


@dp.message_handler(commands=['gadget_safety'])
async def gadjet_safety(message: types.Message):
    text = "<b>Ґаджет Безпека</b>\n\n" \
           "<b>90 грн/12 тижнів</b>\n\n" \
           "<b>В пакеті:</b>\n" \
           "   - 150 МБ інтернету\n" \
           "   - Дзвінки: 15 хв\n" \
           " - 15 SMS/день\n\n" \
           "Більше інформації <a href='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-bezpeka/'>тут</a>"

    await message.reply(text, parse_mode=types.ParseMode.HTML)
    await bot.send_invoice(message.chat.id,
                           'Поповнення рахунку',
                           'ґаджет Безпека',
                           'invoice',
                           password.PAYMENT_TOKE,
                           'UAH',
                           [types.LabeledPrice('Поповнення рахунку', 90 * 100)]
                           )


@dp.message_handler(commands=['gadget_smart'])
async def gadget_smart(message: types.Message):
    text = "<b>Ґаджет Смарт</b>\n\n" \
           "<b>150 грн/4 тижні</b>\n\n" \
           "<b>В пакеті:</b>\n" \
           "   - 500 МБ інтернету\n" \
           "   - Дзвінки: 50 хв\n" \
           " - 50 SMS/день\n\n" \
           "Більше інформації <a href='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/'>тут</a>"

    await message.reply(text, parse_mode=types.ParseMode.HTML)
    await bot.send_invoice(message.chat.id,
                           'Поповнення рахунку',
                           'Ґаджет Смарт',
                           'invoice',
                           password.PAYMENT_TOKE,
                           'UAH',
                           [types.LabeledPrice('Поповнення рахунку', 150 * 100)]
                           )


@dp.message_handler(commands=['gadget_tablet'])
async def gadget_tablet(message: types.Message):
    text = "<b>Ґаджет Планшет</b>\n\n" \
           "<b>275 грн/4 тижні</b>\n\n" \
           "<b>В пакеті:</b>\n" \
           "   - 50 ГБ інтернету\n" \
           " - Вигода до 15% з послугою «Тарифна підписка»\n\n" \
           "Більше інформації <a href='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-tab21/'>тут</a>"

    await message.reply(text, parse_mode=types.ParseMode.HTML)
    await bot.send_invoice(message.chat.id,
                           'Поповнення рахунку',
                           'Ґаджет Планшет',
                           'invoice',
                           password.PAYMENT_TOKE,
                           'UAH',
                           [types.LabeledPrice('Поповнення рахунку', 275 * 100)]
                           )


@dp.message_handler(commands=['gadget_router'])
async def gadget_router(message: types.Message):
    text = "<b>Ґаджет Роутер</b>\n\n" \
           "<b>375 грн/4 тижні</b>\n\n" \
           "<b>В пакеті:</b>\n" \
           " - Iнтернет: Безліміт\n\n" \
           "Більше інформації <a href='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-rout21/'>тут</a>"

    await message.reply(text, parse_mode=types.ParseMode.HTML)
    await bot.send_invoice(message.chat.id,
                           'Поповнення рахунку',
                           'Ґаджет Роутер',
                           'invoice',
                           password.PAYMENT_TOKE,
                           'UAH',
                           [types.LabeledPrice('Поповнення рахунку', 375 * 100)]
                           )


@dp.message_handler(content_types=types.ContentTypes.SUCCESSFUL_PAYMENT)
async def successful_pay(message: types.Message):
    await message.answer(f'Successful: {message.successful_payment.order_info}')


executor.start_polling(dp)
