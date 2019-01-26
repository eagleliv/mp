import asyncio
from channels.consumer import AsyncConsumer
import json

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connection successfull', event)
        await self.send ({
            'type': 'websocket.accept',
        })
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print()
        print(self.room_name)
        print()
        # self.chat_room_name = 'chat_' + room_name
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )cc

    async def websocket_receive(self, event):
        chat_text_raw = event.get('text')
        handled_text = json.loads(chat_text_raw)
        chat_text = handled_text['chat_text']
        user = handled_text['user']
        print(handled_text, chat_text, user)
        message = {
            'message': chat_text,
            'user': user
        }
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'text': json.dumps(message)
            }
        )

    async def chat_message(self, event):
        print(event, 'fff')
        await self.send({
            'type': 'websocket.send',
            'text_data': event['text']
        })
