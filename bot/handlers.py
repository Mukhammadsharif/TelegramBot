from bot.keyboards import send_contact, booking_menu, send_location, location_menu, confirm_menu, \
    who_are_you, yes_or_no
from .booking import after_booking_
from .get_answer_from_drivers import get_answer_from_drivers
from .mark import mark_ser
from .models import Users, Booking, Driver
from .text import booking_type_list


def start(chat, **kwargs):
    if Booking.objects.all():
        booking_object = Booking.objects.get(chat_id=chat.chat_id)
        if booking_object:
            booking_object.delete()
    chat.send_message(f'Добро пожаловать на Такси бот, {chat.first_name}!')
    chat.send_message('Пожалуйста, укажите ваше пользовательское положение', reply_markup=who_are_you())


def registering_user(chat, message, redirect, *args, **kwargs):
    message = message.text
    if message == 'Поссажирь 🤵':
        if not Users.objects.filter(chat_id=chat.chat_id):
            Users.objects.get_or_create(type=chat.type, first_name=chat.first_name, chat_id=chat.chat_id,
                                        username=chat.username)
            chat.send_message(f'Добро пожаловать на Такси бот, {chat.first_name}!', reply_markup=send_contact())
        else:
            chat.send_message(f'Рад вас снова видеть, {chat.first_name}!')
            if Users.objects.get(chat_id=chat.chat_id).number:
                chat.send_message(f'Откуда вас забрать {chat.first_name}?', reply_markup=send_location())
            else:
                chat.send_message('Отправьте ваши контакты', reply_markup=send_contact())


def registering_driver(chat, message, *args, **kwargs):
    message = message.text
    if message == 'Водитель 👨‍✈️':
        if not Driver.objects.filter(chat_id=chat.chat_id):
            Driver.objects.get_or_create(first_name=chat.first_name, chat_id=chat.chat_id,
                                         username=chat.username)
            chat.send_message(f'Добро пожаловать на Такси бот, {chat.first_name}!', reply_markup=send_contact())
        elif Driver.objects.filter(chat_id=chat.chat_id):
            chat.send_message(f'Вы готовы поработать, {chat.first_name}?', reply_markup=yes_or_no())


def ask_confirming(chat, message, *args, **kwargs):
    if message.text == 'Да':
        chat.send_message('Ждите скоро появиться заказы')
        driver = Driver.objects.get(chat_id=chat.chat_id)
        driver.ready = True
        driver.save()

    elif message.text == 'Нет':
        chat.send_message('Ничего, обращайтесь в следуещей раз, мы будем вас ждать!')


def ask_number_from_driver(chat, phone, *args, **kwargs):
    if Driver.objects.filter(chat_id=chat.chat_id):
        driver = Driver.objects.get(chat_id=chat.chat_id)
        driver.number = phone
        driver.save()
        chat.send_message(f'Укажите марка машины')


def ask_car(chat, message, *args, **kwargs):
    driver = Driver.objects.get(chat_id=chat.chat_id)
    driver.car = message.text
    driver.save()
    chat.send_message(f'Укажите номер машины')


def ask_number_of_car(chat, message, *args, **kwargs):
    driver = Driver.objects.get(chat_id=chat.chat_id)
    driver.number_of_car = message.text
    driver.save()
    chat.send_message(f'Укажите цвет машины')


def ask_color(chat, message, *args, **kwargs):
    driver = Driver.objects.get(chat_id=chat.chat_id)
    driver.color_of_car = message.text
    driver.save()
    chat.send_message(f'Ваши данные сохранены')
    chat.send_message(f'Вы готовы поработать, {chat.first_name}?', reply_markup=yes_or_no())


def ask_number(chat, phone, *args, **kwargs):
    user = Users.objects.get(chat_id=chat.chat_id)
    user.number = phone
    user.save()
    chat.send_message(f'Откуда вас забрать {chat.first_name}?', reply_markup=send_location())


def ask_location(chat, location, *args, **kwargs):
    Booking.objects.get_or_create(latitude_from=location['latitude'], longitude_from=location['longitude'],
                                  chat_id=chat.chat_id)
    chat.send_message('Укажите куда вы хотите?', reply_markup=location_menu())
    chat.send_message('Если можете указать по карте, то перейдите в раздел🔗 и нажмите на Location')
    chat.send_message('А если нет просто нажмите на кнопку и напишите направление')


def ask_direction(chat, message, *args, **kwargs):
    if message.text == 'Указать вручную(письменно) ✒':
        chat.send_message('Напишите ориентир или точную адрес')


def booking_text(chat, message, *args, **kwargs):
    if not message.text == 'Указать вручную(письменно) ✒':
        Booking.objects.filter(chat_id=chat.chat_id).update(address_text=message.text)
        chat.send_message('Ваш путь известен, выберете тип услуги', reply_markup=booking_menu())
    else:
        chat.send_message('Напишите ориентир или точную адрес')


def booking_coordinate(chat, message, location, *args, **kwargs):
    if not message.text == 'Указать вручную(письменно) ✒':
        Booking.objects.filter(chat_id=chat.chat_id).update(address_latitude=location['latitude'],
                                                            address_longitude=location['longitude'])
        chat.send_message('Ваш путь известен, выберете тип услуги', reply_markup=booking_menu())
        chat.send_message(f'{booking_type_list()}')
    else:
        chat.send_message('Напишите ориентир или точную адрес')


def booking_answer(chat, message, *args, **kwargs):
    message = message.text
    type_list = ['Быстро 🚀', 'Комфорт 🚕', 'Комфорт+ 🚖', 'Детский 🛴', 'Грузавой 🚚', 'Доставка 🚛']
    for i in type_list:
        if message == i:
            Booking.objects.filter(chat_id=chat.chat_id).update(type=message)
            chat.send_message(f'Вы выбрали тип услуги: {message}')
            chat.send_message(f'{chat.first_name}, вы согласны?', reply_markup=confirm_menu())


def after_booking(chat, message, *args, **kwargs):
    after_booking_(chat, message, *args, **kwargs)


def mark_service(chat, callback_data, *args, **kwargs):
    mark_ser(chat, callback_data, *args, **kwargs)


def get_answer_from_driver(chat, callback_data, *args, **kwargs):
    get_answer_from_drivers(chat, callback_data, *args, **kwargs)


def ask_next_booking(chat, message, *args, **kwargs):
    if message.text == 'Готовo, жду новые заказы 🔎':
        Driver.objects.filter(chat_id=chat.chat_id).update(busy=False)
        chat.send_message('Ждите новые заказы')
    else:
        chat.send_message('Как пожелаете, будем вас ждать')

