<<<<<<< HEAD
"""
WSGI config for SimuladorOperacoes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SimuladorOperacoes.settings.base')

application = get_wsgi_application()
=======
"""
WSGI config for SimuladorOperacoes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SimuladorOperacoes.settings')

application = get_wsgi_application()
>>>>>>> ff6a3c90b9141ef6edc7254235d24cf57f2487b3