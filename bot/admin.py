from django.contrib import admin

# Register your models here.
from bot.models import Users, Booking, BookingHistory, Driver


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'type', 'username', 'first_name', 'number', 'data', 'last_activity']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'latitude_from', 'longitude_from', 'address_text', 'type', 'mark',
                    'address_latitude', 'address_longitude', 'customer', 'number_of_customer'
                    ]


@admin.register(BookingHistory)
class BookingHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'latitude_from', 'longitude_from', 'address_text', 'type', 'mark',
                    'address_latitude', 'address_longitude'
                    ]


@admin.register(Driver)
class Driver(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'username', 'first_name', 'number', 'car', 'color_of_car', 'number_of_car',
                    'busy', 'ready']
