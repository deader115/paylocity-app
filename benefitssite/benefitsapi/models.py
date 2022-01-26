from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=60)
    cost = models.DecimalField(decimal_places=2, max_digits=9)  # per paycheck

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=60)
    reduction = models.DecimalField(
        decimal_places=2, max_digits=3)  # ex. .10 == 10% discount

    def __str__(self):
        return self.name


class Employee(models.Model):
    firstName = models.CharField(max_length=60)
    middleName = models.CharField(max_length=60, blank=True)
    lastName = models.CharField(max_length=60)
    salary = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return f"{self.lastName}, {self.firstName} {self.middleName}".rstrip()


class Dependent(models.Model):
    firstName = models.CharField(max_length=60)
    middleName = models.CharField(max_length=60, blank=True)
    lastName = models.CharField(max_length=60)
    # for now, comp key of employee first, mid, last .lower
    # TODO: Foreign, composite key?
    providerID = models.CharField(max_length=180)

    def __str__(self):
        return f"{self.lastName}, {self.firstName} {self.middleName}".rstrip()
