from botmother.querysets import chat
from botmother.utils.keyboards import *


def who_are_you():
    return keyboard([
        [button('Поссажирь 🤵'), button('Водитель 👨‍✈️')]
    ])


def yes_or_no():
    return keyboard([
        [button('Да'), button('Нет')]
    ])


def mark_buttons():
    return inline_keyboard([
        [inline('Хорошо 👍', {'value': True}, 'mark')],
        [inline('Не очень! 👎', {'value': False}, 'mark')]
    ])


def send_contact():
    return keyboard([
        [button('Отправить номер телефона 🌐', contact=True)],
    ])


def send_location():
    return keyboard([
        [button('Отправить локацию 🏁', location=True)],
    ])


def booking_menu():
    return keyboard([
        [button('Быстро 🚀')],
        [button('Комфорт 🚕')],
        [button('Комфорт+ 🚖')],
        [button('Детский 🛴')],
        [button('Грузавой 🚚')],
        [button('Доставка 🚛')]
    ])


def location_menu():
    return keyboard([
        [button('Указать вручную(письменно) ✒')]
    ])


def confirm_menu():
    return keyboard([
        [button('Да ✔')],
        [button('Нет, я отменяю заказ ❌')]
    ])


def start_menu():
    return keyboard([
        [button('/start')],
        [button('/support')],
        [button('/help')]
    ])


def ready_again():
    return keyboard([
        [button('Готовo, жду новые заказы 🔎')],
        [button('На сегодня хватит 📈')]
    ])
