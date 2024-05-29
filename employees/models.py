from django.db import models

# Create your models here.


class Employee(models.Model):
  user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
  vendor = models.ForeignKey('vendors.Vendor', on_delete=models.CASCADE)
