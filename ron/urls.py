from django.urls import path
from .views import RonChatView

urlpatterns = [
    path("chat/", RonChatView.as_view(), name="ron-chat"),
]