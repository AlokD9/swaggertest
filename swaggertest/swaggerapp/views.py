from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .serilzers import EmpSerilizers,AddressSerilizers
from .models import Employee,Address

class EmpViewSet(ModelViewSet):
    serializer_class =EmpSerilizers
    queryset =Employee.objects.all()

class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerilizers
    queryset = Address.objects.all()