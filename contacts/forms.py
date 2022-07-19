from django import forms
from .models import SendContacts
from captcha.fields import CaptchaField


my_default_errors = {"invalid": "Вы не прошли проверку на человека"}


class ContactFormAnonumus(forms.ModelForm):
    captcha = CaptchaField(label="Код проверки", error_messages=my_default_errors)

    class Meta:
        model = SendContacts
        fields = "__all__"


class ContactFormUser(forms.ModelForm):
    captcha = CaptchaField(label="Код проверки", error_messages=my_default_errors)

    class Meta:
        model = SendContacts
        fields = ("title", "text", "captcha")
