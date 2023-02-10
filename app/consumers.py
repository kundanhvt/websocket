from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer

class MyWebSocketConsumer(WebsocketConsumer):
    def connect(self):
        print('Websocket Connected ...')
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print('Message Received..',text_data)
        self.send(text_data="Message from server to cliend")

    def disconnect(self, code):
        print('Websocket disconnected...')