"""
WSGI config for OfficialWebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/nvic/OfficialWebsite'
if path not in sys.path:
	sys.path.append(path)

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFileHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OfficialWebsite.settings")

application = get_wsgi_application()
