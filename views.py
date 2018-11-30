# coding=utf-8
from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

class WomanView(TemplateView):
    template_name = "woman.html"

class ManView(TemplateView):
    template_name = "man.html"

class СalculatorView(TemplateView):
    template_name = "calculator.html"




