from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

@api_view()
def home(request):
	student_objs = Student.objects.all()
	serializer = StudentSerializer(student_objs, many=True)
	return Response({'status': 200, 'payload': serializer.data})


@api_view(['POST'])
def post_student(request):
	data = request.data
	serializer = StudentSerializer(data=request.data)
	# if request.data['age'] < 18:
	# 	return Response({'status':403, 'message': 'age must be > 18'})
	if not serializer.is_valid():
		return Response({'status': 403, 'errors':serializer.errors, 'message': 'Something went wrong'})

	serializer.save()


	return Response({'status': 200, 'payload': data, 'message':'You sent'})

@api_view(['PUT'])
def update_student(request):
	try:
		student_obj = Student.objects.get(id=id)