import debug_toolbar

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from article import views
from catalog.views import main_catalog

urlpatterns = [
    path("catalog/", include(("catalog.urls", "catalog"), namespace="catalog")),
    path("cart/", include("cart.urls")),
    path("blog/", include("blog.urls")),
    path("account/", include("account.urls")),
    path("admin/", admin.site.urls),
    path("event/", views.view_event, name="event"),
    path("", views.view_home, name="home"),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path("contacts/", include("contacts.urls")),
    path("catalog_main/", main_catalog, name="main_catalog"),
    path("captcha/", include("captcha.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
