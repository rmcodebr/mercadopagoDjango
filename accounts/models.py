from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission
from vendors.models import Vendor

# Create your models here.


class UserManager(BaseUserManager):
  def create_user(self, email, password=None):
    if not email:
      raise ValueError('É preciso um email')

    user = self.model(email=self.normalize_email(email))
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password):
    user = self.create_user(email, password=password)
    user.is_admin = True
    user.save(using=self._db)
    return user


class User(AbstractBaseUser):
  customer = 1
  employee = 2
  vendor = 3

  ROLE_CHOICES = (
      ('customer', 'Cliente'),
      ('employee', 'Colaborador'),
      ('vendor', 'Vendedor')
  )

  role = models.CharField(
      max_length=15, choices=ROLE_CHOICES, blank=True, null=True)
  email = models.EmailField(max_length=255, unique=True)
  first_name = models.CharField(max_length=200, blank=True, null=True)
  last_name = models.CharField(max_length=200, blank=True, null=True)
  phone_number = models.CharField(max_length=20, blank=True, null=True)
  cpf = models.CharField(max_length=20, blank=True, null=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)

  mercadopago_customer_id = models.CharField(
      max_length=200, blank=True, null=True)

  objects = UserManager()
  USERNAME_FIELD = 'email'

  def __str__(self):
    return self.email

  def has_perm(self, perm, obj=None):
    return True

  def has_module_perms(self, app_label):
    return True

  @property
  def is_staff(self):
    return self.is_admin


class Group(models.Model):
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)


class Group_Permissions(models.Model):
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  permission = models.ForeignKey(Permission, on_delete=models.CASCADE)


class User_Groups(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
