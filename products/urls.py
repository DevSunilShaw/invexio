from django.urls import path
from . import views


urlpatterns = [
	path('', views.product_list, name='product_list'),
	path('api/products/', views.product_list_api),
	path('api/products/create/', views.product_create_api),
]