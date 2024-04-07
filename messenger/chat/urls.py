from django.contrib.auth.views import LogoutView
from allauth.account.views import LoginView
from django.urls import path, include
from rest_framework import routers
from . import views
from .views import profile

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)
router.register(r'chats', views.ChatViewSet)
router.register(r'users', views.UserProfileViewSet)

urlpatterns = [
    path('', views.index, name = 'index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('login/', LoginView.as_view(success_url = '/'), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = '/chat'), name = 'logout'),
    path('private_user_page/', profile, name = 'private_user_page'),
]
