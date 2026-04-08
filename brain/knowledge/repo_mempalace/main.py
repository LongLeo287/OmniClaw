import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'omniclaw.settings')
import django
django.setup()
from django.core.management import execute_from_command_line
if __name__ == '__main__':
    execute_from_command_line(['manage.py', 'runserver'])