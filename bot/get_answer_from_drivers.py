import json

import requests

from bot.keyboards import mark_buttons, ready_again
from bot.models import Booking, Driver


def get_answer_from_drivers(chat, callback_data, *args, **kwargs):
    if callback_data['value']:
        booking_object = Booking.objects.get(id=callback_data['id'])
        chat_id_for_api = booking_object.chat_id
        driver = Driver.objects.get(chat_id=chat.chat_id)
        if booking_object:
            data = {"chat_id": chat_id_for_api,
                    "text": 'К вам едет такси: \n \n'
                            f'Марка машины: {driver.car} \n \n'
                            f'Цвет машины: {driver.color_of_car} \n \n'
                            f'Номер машины: {driver.number_of_car} \n \n'
                            f'Номер водителья: +{driver.number} \n \n'
                            f'Водитель: {driver.first_name} \n \n'
                            f'Счастливово пути!!!',
                    "reply_markup": json.dumps(mark_buttons())
                    }
            requests.post(
                url=f'https://api.telegram.org/bot1872394095:AAFK-oDIkjsvXHB8Yv20z0YkUmgTubXl8Gk'
                    f'/sendMessage', data=data).json()
            Driver.objects.filter(chat_id=chat.chat_id).update(busy=True)
            chat.send_message('Клиент вас ожидает')
            chat.send_message('После завершения заказа, объявите нам', reply_markup=ready_again())
        else:
            chat.send_message('Ждите новые заказы')
    else:
        Driver.objects.filter(chat_id=chat.chat_id).update(busy=False)
        chat.send_message('Ждите новые заказы')