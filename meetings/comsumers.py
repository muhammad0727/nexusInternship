import json
import channels.generic.websocket import AsyncWebsocketConsumer

class VideoCallConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'video_call_{self.room_name}' # some discrepency here.

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'video_call_message',
                'message': message,
                'sender_channel_name': self.channel_name,
            }
        )

    async def video_call_message(self, event):
        message = event['message']

        # Send message to WebSocket
        if self.channel_name != event['sender_channel_name']:
            await self.send(text_data=json.dumps({
                'message': message
            }))