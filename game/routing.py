
from django.urls import path
from . import consumers

ws_patterns = [
    path('ws/sc/',consumers.ForCreatingRoom.as_asgi()),
]