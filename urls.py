from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from hm.views import IndexView, WomanView, ManView, СalculatorView, Woman_categoryView, Woman_productsView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^woman/$', WomanView.as_view(), name="woman"),
    url(r'^man/$', ManView.as_view(), name="man"),
    url(r'^calculator/$', СalculatorView.as_view(), name="calculator"),
    url(r'^woman_category/(?P<woman_category_id>\d+)$', Woman_categoryView.as_view(), name="woman_category"),
    url(r'^woman_products/(?P<woman_products_id>\d+)$', Woman_productsView.as_view(), name="woman_products"),

    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
