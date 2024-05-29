from django.shortcuts import render

# Create your views here.


def payments(request):
  return render(request, 'payments/payments.html')


def create_customer(request):
  return render(request, 'payments/create_customer.html')
