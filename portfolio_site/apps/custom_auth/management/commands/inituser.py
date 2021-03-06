from django.core.management import BaseCommand
from django.db import IntegrityError

from apps.custom_auth.enums import RoleTypes
from apps.custom_auth.models import User


class Command(BaseCommand):
    help = 'Create initial admin user with all permissions'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Account username *must be unique')
        parser.add_argument('email', type=str, help='Account email')
        parser.add_argument('password', type=str, help='Account password')

    def handle(self, *args, **kwargs):

        try:
            user = User.objects.create(
                username=kwargs['username'],
                email=kwargs['email'],
            )
            user.set_password(kwargs['password'])
            user.is_draft = True
            user.is_superuser = True  # assess to the administrative pannel
            user.role = RoleTypes.ADMINISTRATOR
            user.save()
            msg = 'Account "username" suscessfully created.'.format(username=user.username)
        except IntegrityError:
            msg = 'User with this username already exists.'

        self.stdout.write(msg)
