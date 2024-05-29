from django.db import models

# Create your models here.


class Vendor(models.Model):
  user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  address = models.CharField(max_length=200, blank=True, null=True)
