from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, 'usercv/index.html')


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    fields = '__all__'


def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('usercv:user-profile')
    return render(request, 'registration/register.html', {'form': form})


def user_profile(request):
    prof = Profile.objects.get(user=request.user)
    return render(request, 'usercv/user_profile.html', {'prof': prof})




