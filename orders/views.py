from django.shortcuts import render
from .models import Order
from django.contrib import messages
from django.core.paginator import Paginator

def order_list(request):
	order_list = Order.objects.all().order_by('-id')
	paginator = Paginator(order_list, 5)
	page_number = request.GET.get('page')
	Orders = paginator.get_page(page_number)

	context = {
		'Orders': Orders
	}

	return render(request, 'orders/order_list.html', context)

