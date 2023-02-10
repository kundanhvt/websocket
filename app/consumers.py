from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep
import asyncio
from asgiref.sync import async_to_sync
import json
from .models import Group, Chat
class MyWebSocketConsumer(WebsocketConsumer):
    def connect(self):
        print('Websocket Connected ...')
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data["msg"]
        group = Group.objects.get(name= self.group_name)
        chat = Chat(chat = data['msg'],group = group)
        chat.save()
        async_to_sync(self.channel_layer.group_send)(self.group_name,{'type':'chat.message','message':message})
        
    def chat_message(self, event):
        self.send(text_data = json.dumps({
            'msg':event['message']
        }))

    def disconnect(self, code):
        print('Websocket disconnected...')
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_layer
        )


class MyAsyncWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('Websocket Connected ...')
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print('Message Received..',text_data)

    async def disconnect(self, close_code):
        print('Websocket Disconnected...', close_code)