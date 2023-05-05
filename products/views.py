from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "products/index.html"


class DetailListview(TemplateView):
    template_name = "products/detail.html"


class ProductListView(TemplateView):
    template_name = "products/shop.html"
