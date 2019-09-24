from rest_framework_mongoengine import viewsets as meviewsets

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeesView(meviewsets.ModelViewSet):
    lookup_field = 'employeeId'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer