from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path(
        "",
        views.view_blog,
        name="blog",
    ),
    path("page/<int:page_id_src>", views.view_page, name="page_blog"),
]
