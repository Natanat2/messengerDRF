from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import SignUpForm, UserProfileForm


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'


def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance = request.user.userprofile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/')
    else:
        form = UserProfileForm(instance = request.user.userprofile)
    return render(request, 'profile.html', {'form': form})
