from django.shortcuts import render
from .models import Expense

def expense_list(request):
	expenses = Expense.objects.all()

	context = {
		'expenses': expenses
	}
	return render(request, 'expense/expense_list.html', context)