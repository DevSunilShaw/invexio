from django.shortcuts import render
from .models import Order


def order_list(request):
	Orders = Order.objects.all()

	context = {
		'Orders': Orders
	}

	return render(request, 'orders/order_list.html', context)

