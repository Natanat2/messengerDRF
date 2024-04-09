from allauth.account.signals import user_signed_up
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from ..chat.models import UserProfile


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'


@receiver(user_signed_up)
def create_user_profile(sender, **kwargs):
    user = kwargs['user']
    UserProfile.objects.create(user = user)
