from rest_framework import serializers
from .models import Employee,Address

class EmpSerilizers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields ='__all__'

class AddressSerilizers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Address
        fields='__all__'
