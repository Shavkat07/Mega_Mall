from django.urls import path
from .views import ProductListView, DetailListview


urlpatterns = [
    path('detail/', DetailListview.as_view(), name='detail'),
    path('shop/', ProductListView.as_view(), name='shop'),
]
