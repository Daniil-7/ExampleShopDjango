from django.shortcuts import render
from article.models import *
from django.views.generic import ListView
from django.db.models import Q
from catalog.models import Product


def saleFun(object_list):
    for i in range(len(object_list)):
        object_list[i].valsale = False
        if object_list[i].sale != 1.0:
            object_list[i].valsale = True
            object_list[i].saleprice = object_list[i].price * object_list[i].sale
            object_list[i].htmlprice = str(100 - object_list[i].sale * 100) + "%"
    return object_list


def saleOneFun(object_list):
    object_list.valsale = False
    if object_list.sale != 1.0:
        object_list.valsale = True
        object_list.saleprice = object_list.price * object_list.sale
        object_list.htmlprice = str(100 - object_list.sale * 100) + "%"
    return object_list


def view_event(request):
    articles = Article.objects.order_by("created")
    products = ArticleProduct.objects.all()
    for i in range(len(products)):
        products[i].products = saleOneFun(products[i].products)

    context = {"articles": articles, "products": products}

    return render(request, "event.html", context)


def view_home(request):
    articles = MainPageArticle.objects.order_by("created")
    products = MainPageArticleProduct.objects.all()
    for i in range(len(products)):
        products[i].products = saleOneFun(products[i].products)

    context = {"articles": articles, "products": products}

    return render(request, "home.html", context)


class SearchResultsView(ListView):
    model = Product
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        object_list = saleFun(object_list)
        return object_list
