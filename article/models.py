from django.db import models

from catalog.models import Product


class Article(models.Model):
    name = models.CharField(max_length=128, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Основной текст")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Акцию"
        verbose_name_plural = "Акции"

    def __str__(self):
        return self.name


class ArticleProduct(models.Model):
    category = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="articalCategorys",
        verbose_name="Раздел",
    )
    products = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="articalProducts",
        verbose_name="Продукт",
    )

    class Meta:
        verbose_name = "Товар акции"
        verbose_name_plural = "Товары акций"

    def __str__(self):
        return self.products.title


class MainPageArticle(models.Model):
    name = models.CharField(max_length=128, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Основной текст")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Событие на главной"
        verbose_name_plural = "События на главной"

    def __str__(self):
        return self.name


class MainPageArticleProduct(models.Model):
    category = models.ForeignKey(
        MainPageArticle,
        on_delete=models.CASCADE,
        related_name="mainPageArticalCategorys",
        verbose_name="Раздел",
    )
    products = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="mainPageArticalProducts",
        verbose_name="Продукт",
    )

    class Meta:
        verbose_name = "Товар события на главной"
        verbose_name_plural = "Товары сoбытий на главной"

    def __str__(self):
        return self.products.title
