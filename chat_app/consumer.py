# import json
# import logging
# from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from jwt import decode as jwt_decode
# from django.conf import settings
# from django.contrib.auth import get_user_model
from urllib.parse import parse_qs
# from channels.db import database_sync_to_async
#
# from channels.generic.websocket import AsyncWebsocketConsumer
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# from rest_framework_simplejwt.tokens import UntypedToken
#
#
# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = f"chat_{self.room_name}"
#         self.channel_layer.group_send(self.room_group_name,
#                                       {"type": "chat_message", "message": "user joined", "user": self.scope["user"]})
#         token = parse_qs(self.scope["query_string"].decode("utf8")).get("token", [None])[0]
#         try:
#             if not token:
#                 raise InvalidToken("Token is missing")
#
#             UntypedToken(token)
#         except (InvalidToken, TokenError) as e:
#             logging.error(f"Token validation failed: {e}")
#             return None
#         else:
#             decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
#             logging.debug(f"Decoded token data: {decoded_data}")
#
#         try:
#             # Get the user using ID
#             user = await database_sync_to_async(get_user_model().objects.get)(id=decoded_data["user_id"])
#         except get_user_model().DoesNotExist:
#             logging.error(f"User not found with ID: {decoded_data['user_id']}")
#             return None
#         print(user)
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
#
#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         print(text_data)
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         user = self.scope["user"]
#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name, {"type": "chat.message", "message": message, "user": user}
#         )
#
#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event["message"]
#         user = self.scope["user"]
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({"message": message, "user": user}))
import json

from channels.generic.websocket import AsyncWebsocketConsumer

from backend_core import settings


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        token = parse_qs(self.scope["query_string"].decode("utf8")).get("token", [None])[0]
        decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user = await database_sync_to_async(get_user_model().objects.get)(id=decoded_data["user_id"])
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = text_data_json["user"]
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, "user": user}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        user = event["user"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "user": user}))
