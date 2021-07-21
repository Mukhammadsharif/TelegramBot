from bot.keyboards import start_menu
from bot.models import Booking


def mark_ser(chat, callback_data, *args, **kwargs):
    print(callback_data)
    if callback_data['value']:
        chat.send_message('Мы ради что вам понравилось', reply_markup=start_menu())
    elif not callback_data['value']:
        chat.send_message('Мы работаем над этим, будем рад услышать ваше мнение и предложение, '
                          'обращаетесь по номеру +998902994774', reply_markup=start_menu())
    else:
        chat.send_message('В следующий раз вам точно понравиться!', reply_markup=start_menu())
    booking_object = Booking.objects.get(chat_id=chat.chat_id)
    booking_object.delete()
