import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        # Join romm group
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

        # Receive message from WebSocket
    async def receive(self, text_data):
        handled_text = json.loads(text_data)
        chat_text = handled_text['chat_text']
        user = handled_text['user']
        message = {
            'message': chat_text,
            'user': user
        }

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'show_text',
                'text': message
            }
        )

    # Receive message from room group
    async def show_text(self, event):
        message = event['text']

        #Send message to WebSocket
        await self.send(text_data = json.dumps({
            'message': message
        }))
