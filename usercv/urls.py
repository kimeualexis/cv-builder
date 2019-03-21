from django.urls import path
from . import views


app_name = 'usercv'

urlpatterns = [
    path('', views.index, name='cv-index'),
    path('<int:pk>/profile-update', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('register', views.signup, name='user-signup'),
    path('user-profile', views.user_profile, name='user-profile'),
    path('<int:pk>/about-update', views.AboutUpdateView.as_view(), name='about-update'),
]


