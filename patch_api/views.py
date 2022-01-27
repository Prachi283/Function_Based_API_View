from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee1
from .serializers import EmployeeSerializer1
from rest_framework import status 
@api_view(['GET','PUT','POST','PATCH','DELETE'])
def Employee_view(request,pk=None):
	if request.method=='GET':
		id=pk
		if id is not None:
			emp=Employee1.objects.get(id=id)
			serializer = EmployeeSerializer1(emp)
			return Response(serializer.data)
	
		emp=Employee1.objects.all()
		serializer=EmployeeSerializer1(emp,many=True)
		return Response(serializer.data)


	if request.method=='POST':
		serializer=EmployeeSerializer1(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	if request.method=="PUT":
		id=pk
		emp=Employee1.objects.get(pk=id)
		serializer=EmployeeSerializer1(emp,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Complete Data is Updated'})
			return Response(serializer.errors)

	if request.method=="PATCH":
		id=pk
		emp=Employee1.objects.get(pk=id)
		serializer=EmployeeSerializer1(emp,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Partial Data is Updated'})
			return Response(serializer.errors)


	if request.method=="DELETE":
		id=pk
		emp=Employee1.objects.get(pk=id)
		emp.delete()
		return Response({'msg':'Data is deleted'})