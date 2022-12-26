from django.db import models


class CheckIn(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=225)
    contact_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    guest_number = models.IntegerField()
    checkIns = models.CharField(max_length=10)
    checkOut = models.CharField(max_length=10)


class CheckOut(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=225)
    contact_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    guest_number = models.IntegerField()
    checkIns = models.CharField(max_length=10)
    checkOut = models.CharField(max_length=10)


