from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from .models import Profile, About
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, 'usercv/index.html')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['image', 'phone', 'email', 'dob', 'website', 'address', 'city']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AboutUpdateView(LoginRequiredMixin, UpdateView):
    model = About
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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
    about = About.objects.get(user=request.user)
    return render(request, 'usercv/user_profile.html', {'about': about, 'prof': prof})








