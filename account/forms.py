from django.contrib.auth.forms import UserCreationForm
from account.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "password1",
            "password2",
        )


class NewEmailProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)


class NewUsernameProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username",)


class NewFullNameProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class NewPhoneProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("phone",)
