from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from rest_framework import viewsets, status

from .services import BenefitsService
from .serializers import EmployeeSerializer
from .models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('lastName')
    serializer_class = EmployeeSerializer

# TODO: Fix CSRF


@csrf_exempt
def previewCost(request):
    return HttpResponse(BenefitsService.calculate_cost(request))


# def lookupCost(request, id):
    # try:
    #     employee = Employee.objects.get(id=id)
    #     return HttpResponse(BenefitsService.lookup_cost(employee))
    # except Employee.DoesNotExist:
    #     return HttpResponse({'message': 'Unable to get cost: Employee does not exist'}, status=status.HTTP_404_NOT_FOUND)
