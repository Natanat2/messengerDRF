from django.urls import path
from .views import SignUp, profile_view

urlpatterns = [
    path('signup', SignUp.as_view(), name = 'signup'),
    path('profile/', profile_view, name = 'profile_view'),
]
