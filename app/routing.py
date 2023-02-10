from django.urls import path
from .import consumers

websocket_urlpatterns = [
    path('ws/awsc/',consumers.MyAsyncWebSocketConsumer.as_asgi()),
    path('ws/wsc/',consumers.MyWebSocketConsumer.as_asgi())
]