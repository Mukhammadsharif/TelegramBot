from botmother.webhook import webhook
from django.urls import path

from .handlers import *


def dispatch(router, *args, **kwargs):
    router.callback('accept', get_answer_from_driver),
    router.command('/start', start),
    router.text('Поссажирь 🤵', registering_user, last_action=[start]),
    router.text('Водитель 👨‍✈️', registering_driver, last_action=[start]),
    router.contact(ask_number_from_driver, last_action=[registering_driver]),
    router.contact(ask_number, last_action=[registering_user]),
    router.any(ask_car, last_action=[ask_number_from_driver]),
    router.any(ask_number_of_car, last_action=[ask_car]),
    router.any(ask_color, last_action=[ask_number_of_car]),
    router.any(ask_confirming, last_action=[ask_color, registering_driver]),
    router.location(ask_location, last_action=[registering_user, ask_number]),
    router.text('Указать вручную(письменно) ✒', ask_direction, last_action=[ask_location, registering_user]),
    router.any(booking_text, last_action=[ask_direction]),
    router.location(booking_coordinate, last_action=[ask_location]),
    router.any(booking_answer, last_action=[booking_text, booking_coordinate]),
    router.any(after_booking, last_action=[booking_answer]),
    router.callback('mark', mark_service),
    router.any(ask_next_booking, last_action=[get_answer_from_driver])


urlpatterns = [
    path('webhook', webhook(dispatch)),
]
