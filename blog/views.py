from django.shortcuts import render
from blog.models import Blog


def view_blog(request):
    blogs = Blog.objects.all()[::-1]
    context = {"blogs": blogs}
    return render(request, "blog.html", context)


def view_page(request, page_id_src):
    page = Blog.objects.filter(id=page_id_src)
    context = {"pages": page}
    return render(request, "blogPage.html", context)
