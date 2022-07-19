from django.db import models
from tinymce.models import HTMLField
import cloudinary.models
import cloudinary
from diplom_django_netology import configure


cloudinary.config(
    cloud_name=configure.cloudinary_cloud_name,
    api_key=configure.cloudinary_api_key,
    api_secret=configure.cloudinary_api_secret,
)


class Blog(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=128, verbose_name="Заголовок")
    image = cloudinary.models.CloudinaryField(verbose_name="Изображение")
    content = HTMLField(verbose_name="Текст")

    class Meta:
        verbose_name = "Статью"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
