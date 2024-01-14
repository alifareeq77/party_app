import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.channel_layer.group_send(self.room_group_name,
                                      {"type": "chat_message", "message": "user joined", "user": self.scope["user"]})
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.scope["user"]
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, "user": user}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        user = self.scope["user"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "user": user}))
