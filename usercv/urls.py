from django.urls import path
from . import views


app_name = 'usercv'

urlpatterns = [
    path('', views.index, name='cv-index'),
    path('<int:pk>/profile-update', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('register', views.signup, name='user-signup'),
    path('user-profile', views.user_profile, name='user-profile'),
    path('about-create', views.AboutCreateView.as_view(), name='about-create'),
    path('<int:pk>/about-update', views.AboutUpdateView.as_view(), name='about-update'),
    path('education-create', views.EducationCreateView.as_view(), name='education-create'),
    path('<int:pk>/education-update', views.EducationUpdateView.as_view(), name='education-update'),
    path('career-create', views.CareerCreateView.as_view(), name='career-create'),
    path('<int:pk>/career-update', views.CareerUpdateView.as_view(), name='career-update'),
    path('course-create', views.CourseCreateView.as_view(), name='course-create'),
    path('<int:pk>/course-update', views.CourseUpdateView.as_view(), name='course-update'),
    path('experience-create', views.ExperienceCreateView.as_view(), name='experience-create'),
    path('<int:pk>/experience-update', views.ExperienceUpdateView.as_view(), name='experience-update'),
    path('portfolio-create', views.PortfolioCreateView.as_view(), name='portfolio-create'),
    path('<int:pk>/portfolio-update', views.PortfolioUpdateView.as_view(), name='portfolio-update'),
    path('skill-create', views.SkillCreateView.as_view(), name='skill-create'),
    path('<int:pk>/skill-update', views.SkillUpdateView.as_view(), name='skill-update'),
    path('hobby-create', views.HobbyCreateView.as_view(), name='hobby-create'),
    path('<int:pk>/hobby-update', views.HobbyUpdateView.as_view(), name='hobby-update'),
    path('language-create', views.LanguageCreateView.as_view(), name='language-create'),
    path('<int:pk>/language-update', views.LanguageUpdateView.as_view(), name='language-update'),
    path('cocurricular-create', views.CocurricularCreateView.as_view(), name='cocurricular-create'),
    path('<int:pk>/cocurricular-update', views.CocurricularUpdateView.as_view(), name='cocurricular-update'),
    path('reference-create', views.ReferenceCreateView.as_view(), name='reference-create'),
    path('<int:pk>/reference-update', views.ReferenceUpdateView.as_view(), name='reference-update'),

    path('create_cv', views.cv_view, name='create-cv'),
]


