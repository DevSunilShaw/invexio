from django.shortcuts import render
from .models import Inventory

def inventory_list(request):
	inventories = Inventory.objects.all()

	context = {
		'inventories': inventories
	}
	return render(request, 'inventories/inventory_list.html', context)
