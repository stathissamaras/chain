"""
WSGI config for chain project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
import sys
import os

# Add this line
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chain.settings')

application = get_wsgi_application()
