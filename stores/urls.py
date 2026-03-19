from django.urls import path
from .views import store_list
# from .serializers import store_list_api, store_create_api

urlpatterns = [
	path('', store_list, name='store_list'),
	# path('api/sores/', views.store_list_api),
	# path('api/sores/create/', views.store_create_api),

]