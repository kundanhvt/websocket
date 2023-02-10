from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep
import asyncio

class MyWebSocketConsumer(WebsocketConsumer):
    def connect(self):
        print('Websocket Connected ...')
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print('Message Received..',text_data)
        for i in range(20):
            sleep(1)
            self.send(text_data=str(i))

    def disconnect(self, code):
        print('Websocket disconnected...')


class MyAsyncWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('Websocket Connected ...')
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print('Message Received..',text_data)
        for i in range(20):
            await asyncio.sleep(1)
            await self.send(text_data=str(i))

    async def disconnect(self, close_code):
        print('Websocket Disconnected...', close_code)