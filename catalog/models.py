from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
import cloudinary.models
import cloudinary
from diplom_django_netology import configure


cloudinary.config(
    cloud_name=configure.cloudinary_cloud_name,
    api_key=configure.cloudinary_api_key,
    api_secret=configure.cloudinary_api_secret,
)


prSale = []
for i in range(101):
    prSale.append((round(1.0 - i / 100, 2), str(i) + "%"))
prSale = tuple(prSale)


class Category(MPTTModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Категория",
    )

    image = cloudinary.models.CloudinaryField(verbose_name="Изображение (обязательно)")

    slug = models.SlugField(unique=True)

    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="Каталог",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("-id",)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "catalog:product_list_by_category", kwargs={"category_slug": self.slug}
        )


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )

    title = models.CharField(
        max_length=255,
        verbose_name="Наименование",
    )

    description = models.TextField(verbose_name="Описание")

    price = models.FloatField(verbose_name="Цена(в рублях)")

    count = models.IntegerField(verbose_name="Количество")

    sale = models.FloatField(
        choices=prSale,
        max_length=128,
        verbose_name="Скидка в процентах",
        default=prSale[0][0],
    )

    image = cloudinary.models.CloudinaryField(
        verbose_name="Изображение №1 (обязательно)"
    )

    image2 = cloudinary.models.CloudinaryField(
        verbose_name="Изображение №2 (необязательно)", blank=True
    )

    image3 = cloudinary.models.CloudinaryField(
        verbose_name="Изображение №3 (необязательно)", blank=True
    )

    image4 = cloudinary.models.CloudinaryField(
        verbose_name="Изображение №4 (необязательно)", blank=True
    )

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "catalog:product_detail",
            kwargs={"product_slug": self.slug, "category_slug": self.category.slug},
        )


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE, verbose_name="Товар"
    )

    name = models.CharField(
        max_length=64,
        verbose_name="Имя",
    )

    rating = models.PositiveSmallIntegerField(verbose_name="Рейтинг")
    review = models.TextField(max_length=255, verbose_name="Отзыв")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name
