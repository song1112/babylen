"""
WSGI config for babylen project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append(project)
sys.path.append('/home/ubuntu')
os.environ['DJANGO_SETTINGS_MODULE'] = 'babylen.apache.override'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
