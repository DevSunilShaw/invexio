from django.shortcuts import render
from .models import Expense
from django.contrib import messages
from django.core.paginator import Paginator

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


def expense_list(request):
	expenses = Expense.objects.all()

	context = {
		'expenses': expenses
	}
	return render(request, 'expense/expense_list.html', context)


@api_view(['GET'])
@permission_classes([AllowAny])
def expense_list_api(request):
	expenses = Expense.objects.all()

	serializers = ExpenseSerializers(expenses, many=True)
	return Respose(serializers.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def expense_create_api(request):
	serializer = ProductSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Respose(serializer.data)

	return Respose(serializer.errors)