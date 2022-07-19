from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.forms import ReviewForm
from catalog.models import Product, Category


class ProductListView(ListView):
    paginate_by = 9
    context_object_name = "products_list"

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs["category_slug"])
        out = Product.objects.filter(category__slug=self.category.slug).select_related(
            "category"
        )
        return out

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        for i in range(len(context["products_list"])):
            context["products_list"][i].valsale = False
            if context["products_list"][i].sale != 1.0:
                context["products_list"][i].valsale = True
                context["products_list"][i].saleprice = (
                    context["products_list"][i].price * context["products_list"][i].sale
                )
                context["products_list"][i].htmlprice = (
                    str(100 - context["products_list"][i].sale * 100) + "%"
                )
        return context


class ProductDetail(DetailView):
    model = Product
    slug_field = "slug"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        context["form"] = ReviewForm
        context["product"].valsale = False
        if context["product"].sale != 1.0:
            context["product"].valsale = True
            context["product"].saleprice = (
                context["product"].price * context["product"].sale
            )
            context["product"].htmlprice = (
                str(100 - context["product"].sale * 100) + "%"
            )
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST, request.FILES)
        self.object = super(ProductDetail, self).get_object()
        context = super(ProductDetail, self).get_context_data()
        context["form"] = ReviewForm
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.name = request.user.username
            new_review.product = self.object
            new_review.save()

        else:
            context["form"] = form

        context["product"].valsale = False
        if context["product"].sale != 1.0:
            context["product"].valsale = True
            context["product"].saleprice = (
                context["product"].price * context["product"].sale
            )
            context["product"].htmlprice = (
                str(100 - context["product"].sale * 100) + "%"
            )
        return self.render_to_response(context=context)


def main_catalog(request):
    return render(request, "catalog/main_catalog.html")
