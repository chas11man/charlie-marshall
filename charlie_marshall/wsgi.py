"""
WSGI config for charlie_marshall project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "charlie_marshall.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
