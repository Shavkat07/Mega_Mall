from django.urls import path
from .views import CheckoutListView, ContactListView, CartListview

app_name = 'client'

urlpatterns = [
    path('cart/', CartListview.as_view(), name='cart'),
    path('checkout/', CheckoutListView.as_view(), name='checkout'),
    path('contact/', ContactListView.as_view(), name='contact'),
]

