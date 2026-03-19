from django.shortcuts import render
from .models import Product
from django.contrib import messages
from django.core.paginator import Paginator

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


def product_list(request):
	product_list = Product.objects.all().order_by('-id')
	paginator = Paginator(product_list, 5)
	page_number = request.GET.get('page')
	products = paginator.get_page(page_number)

	context = {
		'products': products
	}

	return render(request, 'products/product_list.html', context)


def product_creation(request):
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("product_list")
	else:
		form = ProductForm()

	return render(request, "product/product_form.html", {"form":form})


def product_update(request, pk):
	product = Product.objects.get(id=pk)

	form = ProductForm(request.POST or None, instance=product)

	if form.is_valid():
		form.save()
		return redirect("product_list")

	return render(request, "products/product_form.html", {"form":form})
	
@api_view(['GET'])
@permission_classes([AllowAny])
def product_list_api(request):
	products = Product.objects.all()
	serializers = ProductSerializer(products, many=True)
	return Response(serializers.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def product_create_api(request):
	serializer = ProductSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)

	return Response(serializer.errors)