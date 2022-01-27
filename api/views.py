from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
# @api_view()
# def hello_world(request):
# 	return Response({'msg':'Hello World'})

# @api_view(['POST'])
# def hello_world(request):
# 	if request.method=="POST":
# 		print(request.data)
# 		return Response({'msg':'POST request- Hello World'})

# @api_view(['GET','POST'])
# def hello_world(request):
# 	if request.method=="GET":
# 		print(request.data)
# 		return Response({'msg':'GET request- Hello World'})

# 	if request.method=="POST":
# 		print(request.data)
# 		return Response({'msg':'POST request- Hello World', 'data':request.data})

@api_view(['GET','PUT','POST','DELETE'])
def Emp_view(request):
	if request.method=='GET':
		id=request.data.get('id')
		if id is not None:
			emp=Employee.objects.get(id=id)
			serializer = EmployeeSerializer(emp)
			return Response(serializer.data)
	
		emp=Employee.objects.all()
		serializer=EmployeeSerializer(emp,many=True)
		return Response(serializer.data)


	if request.method=='POST':
		serializer=EmployeeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Data created'})
		return Response(serializer.errors)

	if request.method=="PUT":
		id=request.data.get('id')
		emp=Employee.objects.get(pk=id)
		serializer=EmployeeSerializer(emp,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Data is Updated'})
			return Response(serializer.errors)

	if request.method=="DELETE":
		id=request.data.get('id')
		emp=Employee.objects.get(pk=id)
		emp.delete()
		return Response({'msg':'Data is deleted'})