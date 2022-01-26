
import json
from typing import List
from django.http import JsonResponse

from .models import Employee


class BenefitsService:

    EMPLOYEE_SALARY = 52000.00
    PAY_PERIODS = 26
    DISCOUNT_REDUCTION = .1
    DEPENDENT_BASE_COST = 500
    EMPLOYEE_BASE_COST = 1000

    @staticmethod
    def get_employee_cost(employee) -> float:
        reduction = 0
        isAName = employee.get('firstName').lower().startswith('a')
        if isAName:
            # TODO: lookup discount in db
            reduction = .1
        return BenefitsService.EMPLOYEE_BASE_COST * (1 - reduction)

    @staticmethod
    def get_dependents_cost(employee) -> float:
        # TODO: type the request?
        dependents = employee.get('dependents')
        dependentCost = 0.0

        for dependent in dependents:
            reduction = 0
            isAName = dependent.get('depFirstName').lower().startswith('a')
            if isAName:
                # TODO: lookup discount in db
                reduction = BenefitsService.DISCOUNT_REDUCTION
            dependentCost += BenefitsService.DEPENDENT_BASE_COST * \
                (1 - reduction)

        return dependentCost

    @staticmethod
    def calculate_cost(request):
        totalCost = 0.0

        employee = json.loads(request.body.decode("utf-8"))
        employeeCost = BenefitsService.get_employee_cost(employee)
        dependentCost = BenefitsService.get_dependents_cost(employee)
        totalCost = employeeCost + dependentCost
        yearCost = totalCost * BenefitsService.PAY_PERIODS
        netSalary = BenefitsService.EMPLOYEE_SALARY - yearCost
        grossPay = BenefitsService.EMPLOYEE_SALARY/BenefitsService.PAY_PERIODS
        netPay = grossPay-totalCost

        response = {"totalCostPerPay": totalCost, "totalCostPerYear": yearCost, "grossSalary": BenefitsService.EMPLOYEE_SALARY, "netSalary": netSalary,
                    "grossPay": grossPay, "netPay": netPay, "employeeCost": employeeCost, "dependentCost": dependentCost, "dependentCount": len(employee.get('dependents'))}
        return JsonResponse(response)

    # TODO: Reuse existing cost method
    # @staticmethod
    # def get_employee_cost_model(employee: Employee) -> float:
    #     reduction = 0
    #     isAName = employee.firstName.lower().startswith('a')
    #     if isAName:
    #         # TODO: lookup discount
    #         reduction = .1
    #     return 1000 * (1 - reduction)

    # # TODO: Reuse existing cost method
    # @staticmethod
    # def get_dependents_cost_model(employee: Employee) -> float:
    #     # TODO: type the request?
    #     dependents = employee.dependents
    #     dependentCost = 0.0

    #     for dependent in dependents:
    #         reduction = 0
    #         isAName = dependent.get('depFirstName').lower().startswith('a')
    #         if isAName:
    #             # TODO: lookup discount
    #             reduction = .1
    #         dependentCost += 500 * (1 - reduction)

    #     return dependentCost

    # # TODO: Fix db, cost methods to pull employee + dependents and calc cost
    # @staticmethod
    # def lookup_cost(employee):
    #     totalCost = 0.0
    #     employeeCost = BenefitsService.get_employee_cost(employee)
    #     dependentCost = BenefitsService.get_dependents_cost(employee)
    #     totalCost = employeeCost + dependentCost
    #     yearCost = totalCost * 26
    #     response = {"totalCostPerPay": totalCost, "totalCostPerYear": yearCost,
    #                 "employeeCost": employeeCost, "dependentCost": dependentCost}
    #     return JsonResponse(response)
