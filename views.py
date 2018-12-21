# coding=utf-8
from django.shortcuts import render
from django.views.generic.base import TemplateView
from hm.models import Subcategories_woman, Categories_woman

class IndexView(TemplateView):
    template_name = "index.html"

class ManView(TemplateView):
    template_name = "man.html"


class СalculatorView(TemplateView):
    template_name = "calculator.html"


class WomanView(TemplateView):
    template_name = "woman.html"

    def get_context_data(self, **kwargs):
        woman = Categories_woman.objects.all()
        return {
            'woman': woman,
        }

class Woman_categoryView(TemplateView):
    template_name = "woman_categoty2.html"

    def get_context_data(self, **kwargs):
        woman_category_id = kwargs['woman_category_id']

        woman_all = Categories_woman.objects.all()
        woman = Categories_woman.objects.get(pk=woman_category_id)
        woman_category = Subcategories_woman.objects.filter(name_сategories=woman_category_id)
        return {
            'woman_all': woman_all,
            'woman': woman,
            'woman_category': woman_category,
        }


class Woman_productsView(TemplateView):
    template_name = "woman_products.html"

    def get_context_data(self, **kwargs):
        woman_products_id = kwargs['woman_products_id']

        woman_products = Subcategories_woman.objects.filter(pk=woman_products_id)
        return {
            'woman_products_id':  woman_products_id,
            'woman_products': woman_products,
        }