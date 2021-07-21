from geopy import Nominatim, Point
from geopy.distance import great_circle
from bot.models import Booking, Users, BookingHistory, Driver
import requests
import json

from bot.views import booking_id, accept_buttons


def after_booking_(chat, message, *args, **kwargs):
    if message.text == 'Да ✔':
        if Booking.objects.all():
            booking_object = Booking.objects.get(chat_id=chat.chat_id)
            user = Users.objects.get(chat_id=chat.chat_id)
            Booking.objects.filter(chat_id=chat.chat_id).update(customer=chat.chat_id, number_of_customer=user.number)
            geolocation = Nominatim(user_agent="bot")
            location_ = geolocation.reverse(f"{booking_object.latitude_from}, {booking_object.longitude_from}")
            old_location = (booking_object.latitude_from, booking_object.longitude_from)
            new_location = (booking_object.address_latitude, booking_object.address_longitude)
            if booking_object.address_text:
                direction = booking_object.address_text
                road_length = 'Неизвестен'
            else:
                geolocation = Nominatim(user_agent="bot")
                location = geolocation.reverse(Point(booking_object.address_latitude, booking_object.address_longitude))
                direction = location.address
                road_length = round(great_circle(old_location, new_location).miles / 0.00062137)
            text = f'  Новый заказ: \n \n' \
                   f'  Откуда: {location_.address} \n \n  ' \
                   f'  Куда:  {direction} \n \n ' \
                   f'  Заказчик: {user.first_name} \n \n' \
                   f'  Длина дороги: {road_length} метр \n \n' \
                   f'  Номер заказчика: +{user.number} \n \n' \
                   f'  Готовы выполнить заказ?'
            booking_id(chat)
            free_drivers = Driver.objects.filter(ready=True, busy=False)
            chat_id_for_api = []
            for i in free_drivers:
                chat_id_for_api.append(i.chat_id)
            for u in chat_id_for_api:
                data = {"chat_id": u,
                        "text": text,
                        "reply_markup": json.dumps(accept_buttons(chat))
                        }
                response = requests.post(
                    url=f'https://api.telegram.org/bot1872394095:AAFK-oDIkjsvXHB8Yv20z0YkUmgTubXl8Gk'
                        f'/sendMessage', data=data).json()
            chat.send_message('Спасибо что выбрали нас, мы выбераем для вас подходящую машину')
            chat.send_message('Оцените нашу услугу после поездки)')
            booking_history_object = BookingHistory.objects.create(
                chat_id=booking_object.chat_id,
                latitude_from=booking_object.latitude_from,
                longitude_from=booking_object.longitude_from,
                address_text=booking_object.address_text,
                address_latitude=booking_object.address_latitude,
                address_longitude=booking_object.address_longitude,
                type=booking_object.type,
                customer=user.first_name,
                number_of_customer=user.number
            )
            booking_history_object.save()
        else:
            chat.send_message('Ничего, обращайтесь в следуещей раз, мы будем вас ждать!')
