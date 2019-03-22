from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView
from .models import Profile, About, Education, Career, Course, Experience, Portfolio, Skill, Hobby, Language, Cocurricular, Reference
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


class AboutCreateView(CreateView):
    model = About
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AboutUpdateView(LoginRequiredMixin, UpdateView):
    model = About
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EducationCreateView(CreateView):
    model = Education
    fields = ['school', 'start', 'end', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EducationUpdateView(UpdateView):
    model = Education
    fields = ['school', 'start', 'end', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CareerCreateView(CreateView):
    model = Career
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CareerUpdateView(UpdateView):
    model = Career
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CourseCreateView(CreateView):
    model = Course
    fields = ['name', 'start', 'end', 'school', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    fields = ['name', 'start', 'end', 'school', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExperienceCreateView(CreateView):
    model = Experience
    fields = ['position', 'company', 'start', 'end', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExperienceUpdateView(UpdateView):
    model = Experience
    fields = ['position', 'company', 'start', 'end', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PortfolioCreateView(CreateView):
    model = Portfolio
    fields = ['name', 'description', 'link', 'cover']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PortfolioUpdateView(UpdateView):
    model = Portfolio
    fields = ['name', 'description', 'link', 'cover']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SkillCreateView(CreateView):
    model = Skill
    fields = ['name', 'description', 'level']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SkillUpdateView(UpdateView):
    model = Skill
    fields = ['name', 'description', 'level']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class HobbyCreateView(CreateView):
    model = Hobby
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class HobbyUpdateView(UpdateView):
    model = Hobby
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LanguageCreateView(CreateView):
    model = Language
    fields = ['name', 'level']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LanguageUpdateView(UpdateView):
    model = Language
    fields = ['name', 'level']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CocurricularCreateView(CreateView):
    model = Cocurricular
    fields = ['activity', 'company', 'start', 'end', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CocurricularUpdateView(UpdateView):
    model = Cocurricular
    fields = ['activity', 'company', 'start', 'end', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReferenceCreateView(CreateView):
    model = Reference
    fields = ['name', 'position', 'company', 'phone', 'email']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReferenceUpdateView(UpdateView):
    model = Reference
    fields = ['name', 'position', 'company', 'phone', 'email']

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
    return render(request, 'usercv/user_profile.html', {'prof': prof})


def cv_view(request):
    abouts = About.objects.filter(user=request.user)
    educations = Education.objects.filter(user=request.user)
    careers = Career.objects.filter(user=request.user)
    courses = Course.objects.filter(user=request.user)
    experiences = Experience.objects.filter(user=request.user)
    portfolios = Portfolio.objects.filter(user=request.user)
    skills = Skill.objects.filter(user=request.user)
    hobbies = Hobby.objects.filter(user=request.user)
    languages = Language.objects.filter(user=request.user)
    cocurriculars = Cocurricular.objects.filter(user=request.user)
    references = Reference.objects.filter(user=request.user)
    context = {
        'abouts': abouts,
        'educations': educations,
        'careers': careers,
        'courses': courses,
        'experiences': experiences,
        'portfolios': portfolios,
        'skills': skills,
        'hobbies': hobbies,
        'languages': languages,
        'cocurriculars': cocurriculars,
        'references': references,
    }
    return render(request, 'usercv/user_cv.html', context)








