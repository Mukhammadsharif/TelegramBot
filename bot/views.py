from botmother.utils.keyboards import inline_keyboard, inline
from django.shortcuts import render

# Create your views here.
from bot.models import Booking


def booking_id(chat, *args, **kwargs):
    booking_object = Booking.objects.get(chat_id=chat.chat_id)
    if booking_object:
        print(booking_object.id)
        return booking_object.id


def accept_buttons(chat):
    return inline_keyboard([
        [inline('Да', {'value': True, 'id': booking_id(chat)}, 'accept')],
        [inline('Нет', {'value': False}, 'accept')]
    ])
