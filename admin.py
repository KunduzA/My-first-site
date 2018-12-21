from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Permission

from hm.models import Categories_woman, Subcategories_woman

class Categories_womanAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

class Subcategories_womanAdmin(ModelAdmin):
    list_display = ["name", "price", "name_сategories"]
    search_fields = ["name"]

admin.site.register(Categories_woman, Categories_womanAdmin)
admin.site.register(Subcategories_woman, Subcategories_womanAdmin)

