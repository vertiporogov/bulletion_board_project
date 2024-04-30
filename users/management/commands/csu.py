import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Функция для создания суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('EMAIL_CSU'),
            first_name=os.getenv('FIRST_NAME_CSU'),
            last_name=os.getenv('LAST_NAME_CSU'),
            role='admin',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        user.set_password(os.getenv('PASSWORD_CSU'))
        user.save()
