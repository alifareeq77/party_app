from django.urls import re_path

from video_app.routing import websocket_urlpatterns2
from . import consumer

websocket_urlpatterns = [
                            re_path(r"ws/chat/(?P<room_name>\w+)/$", consumer.ChatConsumer.as_asgi()),
                        ] + websocket_urlpatterns2
