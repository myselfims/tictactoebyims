"""
ASGI config for tictac project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tictac.settings')
import django

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import game.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tictac.settings')
django.setup()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        game.routing.ws_patterns
    )
})
