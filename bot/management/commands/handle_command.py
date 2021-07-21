# from django.core.management.base import BaseCommand
# from core.models import Chat
#
#
# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         chats = Chat.objects.all()
#         for chat in chats:
#             chat.send_message(
#                 f'{chat.first_name}, как дела? Не желаете узнать погоду? Отправьте команду /<command1>. Если хотите '
#                 f'поменять язык, введите команду /<command2>',
#                 parse_mode="markdown",
#             )