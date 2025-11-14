from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories_list, name='categories_list'),
    path('categories/add/', views.category_create, name='category_add'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),

    path('products/', views.products_list, name='products_list'),
    path('products/add/', views.product_create, name='product_add'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),

    path('credits/', views.credits, name='credits'),
    path('contact/', views.contact, name='contact'),
]
