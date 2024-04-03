from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to = 'images/profile/', null = True, blank = True)

    def __str__(self):
        return self.user.username

    @classmethod
    def update_profile(cls, user, **kwargs):
        profile, created = cls.objects.get_or_create(user = user)
        for key, value in kwargs.items():
            setattr(profile, key, value)
        profile.save()
        return profile


class Chat(models.Model):
    name = models.CharField(max_length = 100)
    users = models.ManyToManyField(User, related_name = 'chats')
    messages = models.ManyToManyField('Message', related_name = 'chat_messages', blank = True)

    def __str__(self):
        return self.name

    @classmethod
    def create_chat(cls, name, users):
        chat = cls.objects.create(name = name)
        chat.users.add(*users)
        return chat

    def edit_chat_name(self, new_name):
        self.name = new_name
        self.save()

    def delete_chat(self):
        self.delete()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete = models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    @classmethod
    def create_message(cls, user, chat, text):
        return cls.objects.create(user = user, chat = chat, text = text)

    def edit_message(self, new_text):
        self.text = new_text
        self.save()

    def delete_message(self):
        self.delete()
