from django.urls import path
from . import views
from . views import ProfileCreateView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'usercv'

urlpatterns = [
    path('', views.index, name='cv-index'),
    path('profile-update', ProfileCreateView.as_view(), name='profile-update'),
    path('register', views.signup, name='user-signup'),
    path('user-profile', views.user_profile, name='user-profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
