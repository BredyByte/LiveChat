from django.urls import path

# consumers files are equivalent to view files but for websocket connection
from a_rtchat.consumers import ChatroomConsumer


websocket_urlpatterns = [
    path("ws/chatroom/<chatroot_name>", ChatroomConsumer.as_asgi()),
]
