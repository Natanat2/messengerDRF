from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from messenger.chat.models import UserProfile


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        UserProfile.objects.create(user=user)
        return response
