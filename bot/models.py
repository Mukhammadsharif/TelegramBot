from django.db import models

# Create your models here.
from botmother.models import AbstractChat


class Chat(AbstractChat):
    class Meta(AbstractChat.Meta):
        db_table = 'bot_chats'


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    chat_id = models.BigIntegerField(null=True, blank=True)
    type = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_action = models.CharField(max_length=255, null=True)
    data = models.TextField(null=True)
    last_activity = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    number = models.BigIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Users"


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    chat_id = models.BigIntegerField(null=True, blank=True)
    latitude_from = models.FloatField(null=True, blank=True)
    longitude_from = models.FloatField(null=True, blank=True)
    address_text = models.CharField(max_length=255, null=True, blank=True)
    address_latitude = models.FloatField(null=True, blank=True)
    address_longitude = models.FloatField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    mark = models.CharField(max_length=255, null=True, blank=True)
    customer = models.CharField(max_length=255, null=True, blank=True)
    number_of_customer = models.BigIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Booking"


class BookingHistory(models.Model):
    id = models.AutoField(primary_key=True)
    chat_id = models.BigIntegerField(null=True, blank=True)
    latitude_from = models.FloatField(null=True, blank=True)
    longitude_from = models.FloatField(null=True, blank=True)
    address_text = models.CharField(max_length=255, null=True, blank=True)
    address_latitude = models.FloatField(null=True, blank=True)
    address_longitude = models.FloatField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    mark = models.CharField(max_length=255, null=True, blank=True)
    customer = models.CharField(max_length=255, null=True, blank=True)
    number_of_customer = models.BigIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "BookingHistory"


class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    chat_id = models.BigIntegerField(null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    number = models.BigIntegerField(null=True, blank=True)
    car = models.CharField(max_length=255, blank=True, null=True)
    color_of_car = models.CharField(max_length=255, blank=True, null=True)
    number_of_car = models.CharField(max_length=255, blank=True, null=True)
    ready = models.BooleanField(default=False)
    busy = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Driver'
