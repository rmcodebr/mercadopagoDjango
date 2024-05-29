from django.contrib.auth.hashers import make_password, check_password
from customers.models import Customer
from employees.models import Employee
from vendors.models import Vendor


User = 'accounts.USer'


class Authentication():
  def signin(self, email=None, password=None):
    user_exists = User.objects.filter(email=email).exists()
    if not user_exists:
      print('Email e/ou senha incorreto(s)')

    user = User.objects.filter(email=email)

    if not check_password(password, user.password):
      print('Email e/ou senha incorreto(s)')

    return user

  def signup(self, email, password, role):
    if not email or email == '':
      print('O email não pode estar vazio')
    if not password or password == '':
      print('O password não pode estar vazio')

    user = User
    if user.objects.filter(email=email).exists():
      print('Este email já existe')

    password_hashed = make_password(password)

    create_user = User.objects.create(
        role=role,
        email=email,
        password=password_hashed)

    if role == 'Vendedor':
      vendor = Vendor.objects.create(
          user=create_user.id)

    if role == 'Cliente':
      Customer.objects.create(
          user=create_user.id)

    if role == 'Cliente':
      Employee.objects.create(
          user=create_user.id,
          vendor=vendor.id)

    return create_user
