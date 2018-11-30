from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from hm.views import IndexView, WomanView, ManView, СalculatorView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^woman/$', WomanView.as_view(), name="woman"),
    url(r'^man/$', ManView.as_view(), name="man"),
    url(r'^calculator/$', СalculatorView.as_view(), name="calculator"),
    path('admin/', admin.site.urls),
]
