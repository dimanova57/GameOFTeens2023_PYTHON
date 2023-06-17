from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


question_zero_button_one = InlineKeyboardButton('Почати', callback_data='question_zero_button_one')

question0 = InlineKeyboardMarkup(resize_keyboard=True).add(question_zero_button_one)

question_one_button_one = InlineKeyboardButton('Для телефону', callback_data='question_one_button_one')
question_one_button_two = InlineKeyboardButton('Для іншого пристрою', callback_data='question_one_button_two')
question_one_button_three = InlineKeyboardButton('Для багатьох людей', callback_data='question_one_button_three')

question1 = InlineKeyboardMarkup(row_width=1)
question1.add(question_one_button_one, question_one_button_two, question_one_button_three)

question_one_button_one = InlineKeyboardButton('Для телефону', callback_data='question_one_button_one')
question_one_button_two = InlineKeyboardButton('Для іншого пристрою', callback_data='question_one_button_two')
question_one_button_three = InlineKeyboardButton('Для багатьох людей', callback_data='question_one_button_three')

question1 = InlineKeyboardMarkup(row_width=1)
question1.add(question_one_button_one, question_one_button_two, question_one_button_three)

question_two_button_one = InlineKeyboardButton('Часто (більше 3-х разів на рік)', callback_data='question_two_button_one')
question_two_button_two = InlineKeyboardButton('Іноді (1-3 рази на рік)', callback_data='question_two_button_two')
question_two_button_three = InlineKeyboardButton('Ніколи (не подорожую за кордоном)', callback_data='question_two_button_three')

question2 = InlineKeyboardMarkup(row_width=1)
question2.add(question_two_button_one, question_two_button_two, question_two_button_three)

question_2second_button_one = InlineKeyboardButton('Дуже часто (кілька разів на день)', callback_data='question_2second_button_one')
question_2second_button_two = InlineKeyboardButton('Кілька разів на тиждень (до 30 хвилин)', callback_data='question_2second_button_two')
question_2second_button_three = InlineKeyboardButton('Рідко (лише у виняткових випадках)', callback_data='question_2second_button_three')

inline_question_2 = InlineKeyboardMarkup(row_width=1)
inline_question_2.add(question_2second_button_one, question_2second_button_two, question_2second_button_three)

question_three_button_one = InlineKeyboardButton('Щодня для всіх цілей (більше 3 годин на день)', callback_data='question_three_button_one')
question_three_button_two = InlineKeyboardButton('Щодня для конкретних цілей (1-3 години на день)', callback_data='question_three_button_two')
question_three_button_three = InlineKeyboardButton('Кілька разів на тиждень (менше 1 години на день)', callback_data='question_three_button_three')
question_three_button_four = InlineKeyboardButton('Рідко використовую Інтернет (тільки по потребі)', callback_data='question_three_button_four')

question3 = InlineKeyboardMarkup(row_width=1)
question3.add(question_three_button_one, question_three_button_two, question_three_button_three, question_three_button_four)

question_four_button_one = InlineKeyboardButton('Так, це важливо для мене', callback_data='question_four_button_one')
question_four_button_two = InlineKeyboardButton('Ні, мені не потрібна безлімітна кількість дзвінків', callback_data='question_four_button_two')

question4 = InlineKeyboardMarkup(row_width=1)
question4.add(question_four_button_one, question_four_button_two)

question_five_button_one = InlineKeyboardButton('Безліміт або велика кількість (понад 20 ГБ)', callback_data='question_five_button_one')
question_five_button_two = InlineKeyboardButton('Від 10 ГБ до 20 ГБ', callback_data='question_five_button_two')
question_five_button_three = InlineKeyboardButton('Від 5 ГБ до 10 ГБ', callback_data='question_five_button_three')
question_five_button_four = InlineKeyboardButton('Менше 5 ГБ', callback_data='question_five_button_four')

question5 = InlineKeyboardMarkup().add(question_five_button_one, question_five_button_two, question_five_button_three, question_five_button_four)

question_six_button_one = InlineKeyboardButton('Так, це важливо для мене', callback_data='question_six_button_one')
question_six_button_two = InlineKeyboardButton('Ні, мені не потрібен пакет послуг для сім`ї',
                                               callback_data='question_six_button_two')
inline_question_6 = InlineKeyboardMarkup().add(question_six_button_one, question_six_button_two)

question_seven_button_one = InlineKeyboardButton('Так, це важливо для мене', callback_data='question_seven_button_one')
question_seven_button_two = InlineKeyboardButton('Ні, мені не потрібен безлімітний доступ до соціальних мереж та месенджерів', callback_data='question_seven_button_two')

inline_question_7 = InlineKeyboardMarkup().add(question_seven_button_one, question_seven_button_two)

question_eight_button_one = InlineKeyboardButton('Так, це важливо для мене', callback_data='question_eight_button_one')
question_eight_button_two = InlineKeyboardButton('Ні, мені не цікава знижка за підписку',
                                                 callback_data='question_eight_button_two')

inline_question_8 = InlineKeyboardMarkup().add(question_eight_button_one, question_eight_button_two)

question_nine_button_one = InlineKeyboardButton('Часто, активно відстежую нові пропозиції', callback_data='question_nine_button_one')
question_nine_button_two = InlineKeyboardButton('Іноді, розглядаю при настанні потреби', callback_data='question_nine_button_two')
question_nine_button_three = InlineKeyboardButton('Рідко, задоволений поточним тарифом', callback_data='question_nine_button_three')
question_nine_button_four = InlineKeyboardButton('Ніколи, не цікавлюся зміною тарифного плану або оператора', callback_data='question_nine_button_four')

inline_question_9 = InlineKeyboardMarkup().add(question_nine_button_one, question_nine_button_two, question_nine_button_three, question_nine_button_four)

question_ten_button_one = InlineKeyboardButton('Щодня або кілька разів на тиждень', callback_data='question_ten_button_one')
question_ten_button_two = InlineKeyboardButton('Раз на тиждень або кілька разів на місяць', callback_data='question_ten_button_two')
question_ten_button_three = InlineKeyboardButton('Рідко, тільки у випадку потреби', callback_data='question_ten_button_three')
question_ten_button_four = InlineKeyboardButton('Ніколи, не перевіряю свій рахунок та витрати на тарифі', callback_data='question_ten_button_four')

inline_question_10 = InlineKeyboardMarkup().add(question_ten_button_one, question_ten_button_two, question_ten_button_three, question_ten_button_four)
