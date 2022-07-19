from django.db import models
from django.core.validators import RegexValidator


class SendMailContacts(models.Model):
    email = models.EmailField(unique=True, verbose_name="Электроная почта")

    class Meta:
        verbose_name = "Почта для получения"
        verbose_name_plural = "Почты для получения"

    def __str__(self):
        return self.email


class SendContacts(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя и Фамилия")
    email = models.EmailField(unique=True, verbose_name="Электроная почта")
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Номер телефона должен быть введен в формате: '+999999999'. Допускается до 15 цифр.",
    )
    phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        verbose_name="Номер телефона",
    )
    title = models.CharField(max_length=255, verbose_name="Тема сообщения")
    text = models.TextField(verbose_name="Cообщение")

    class Meta:
        verbose_name = "Обратная связь(контакты)"
        verbose_name_plural = "Обратная связь(контакты)"

    def __str__(self):
        return self.title
