from django.urls import path
from .import consumers

websocket_urlpatterns = [
    path('ws/asc/',consumers.MyAsyncWebSocketConsumer.as_asgi())
]