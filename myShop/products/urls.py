from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='products-index'),
    path('sale/', views.sale, name='products-sale'),
]