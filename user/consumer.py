import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.chat_room_id = self.scope['url_route']['kwargs']['chat_room_id']
        self.room_group_name = f'chat_{self.chat_room_id}'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        user_id = self.scope['user'].id
        Message.objects.create(chat_room_id=self.chat_room_id, user_id=user_id, content=message)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.scope['user'].username,
            }
        )

    def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))