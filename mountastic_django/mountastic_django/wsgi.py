"""
WSGI config for mountastic_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mountastic_django.settings')

sys.path.append('/home/ubuntu/mountastic/mountastic-api/mountastic_django')
sys.path.append('/home/ubuntu/mountastic/mountastic-api')

application = get_wsgi_application()
