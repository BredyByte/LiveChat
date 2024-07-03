from django.urls import path
from a_rtchat.views import chat_view


app_name = "rtchat"
urlpatterns = [
    path("", chat_view, name="home"),
]
