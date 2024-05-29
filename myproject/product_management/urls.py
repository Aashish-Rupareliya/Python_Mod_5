from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('add_subcategory/', views.add_subcategory, name='add_subcategory'),
    path('search/', views.search_product, name='search_product'),
]
