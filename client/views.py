from django.shortcuts import render
from django.views.generic import TemplateView


class CartListview(TemplateView):
    template_name = "client/cart.html"


class CheckoutListView(TemplateView):
    template_name = "client/checkout.html"


class ContactListView(TemplateView):
    template_name = "client/contact.html"
