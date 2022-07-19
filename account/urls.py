from . import views
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path("register/", views.register, name="register"),
    path("", include("django.contrib.auth.urls")),
    path("profile/newemail/", views.NewEmailProfile, name="profile_newemail"),
    path("profile/newusername/", views.NewUsernameProfile, name="profile_newusername"),
    path("profile/newfullname/", views.NewFullNameProfile, name="profile_newefullname"),
    path("profile/newphone/", views.NewPhoneProfile, name="profile_newphone"),
    path("profile/", views.profile, name="profile"),
]
