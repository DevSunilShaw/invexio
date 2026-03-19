from django.shortcuts import render
from .models import Store

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import StoreSerializer


def store_list(request):
	stores = Store.objects.all()

	context = {
		'stores': stores
	}
	return render(request, 'stores/store_list.html', context)



@api_view(['GET'])
@permission_classes([AllowAny])
def store_list_api(request):
	stores = Store.objects.all()
	serializer = StoreSerializer(store, many=True)
	return Respose(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def store_create_api(request):
	serializer = StoreSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
		return Respose(serializer.data)

	return Respose(serializer.errors)