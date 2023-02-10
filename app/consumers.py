from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json
class MyAsyncWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('Websocket Connected ...')
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print('Message Received..',text_data)
        await self.send(text_data="Message from server to cliend")

    async def disconnect(self, close_code):
        print('Websocket Disconnected...', close_code)