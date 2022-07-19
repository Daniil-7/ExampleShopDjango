from django.contrib import admin

from article.models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name", "created")


@admin.register(ArticleProduct)
class ArticleProductAdmin(admin.ModelAdmin):
    pass


@admin.register(MainPageArticle)
class MainPageArticleAdmin(admin.ModelAdmin):
    list_display = ("name", "created")


@admin.register(MainPageArticleProduct)
class MainPageArticleProductAdmin(admin.ModelAdmin):
    pass
