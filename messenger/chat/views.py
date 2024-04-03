from allauth.account.views import logout, LogoutView

from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, status
from rest_framework import permissions

from .serializers import *



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status = status.HTTP_204_NO_CONTENT)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    chats = Chat.objects.all()
    messages = Message.objects.all()

    context = {
        'chats': chats,
        'messages': messages,
    }
    return render(request, 'index.html', context)


from .models import Chat, Message  # Подключаем модели, которые вам нужны


def private_user_page(request):
    user_chats = Chat.objects.filter(users = request.user)
    user_messages = Message.objects.filter(user = request.user)

    context = {
        'user_chats': user_chats,
        'user_messages': user_messages
    }
    return render(request, 'private_user_page.html', context)


def logout_view(request):
    logout_view = LogoutView.as_view(next_page = '/chat/')
    return logout_view(request)


