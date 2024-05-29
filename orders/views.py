from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
from django.conf import settings
from accounts.models import User

# Create your views here.
MERCADOPAGO_TEST_ACCESS_TOKEN = settings.MERCADOPAGO_TEST_ACCESS_TOKEN


def create_customer(request):
  user = User.objects.get(id=request.user.id)
  if user.phone_number and user.first_name and user.last_name and user.is_active:
    # Customer data
    customer_data = {
        # "email": "customer@example.com",
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone": {
            "area_code": user.phone_number[-11:-9],
            "number": user.phone_number[-9:],
        }
    }
  else:
    return redirect('home')
  print(customer_data)
  # url = 'https://api.mercadopago.com/v1/customers'

  # response = requests.post(url, json=customer_data, headers={
  #                          "Authorization": "Bearer " + MERCADOPAGO_TEST_ACCESS_TOKEN})

  # if response.status_code == 201:
  #   return JsonResponse({"status": "success", "data": response.json()}, status=201)
  # else:
  #   print(response.json())
  #   error_message = response.json().get("message", "Unknown error occurred")
  #   return JsonResponse({"status": "error", "error": error_message, 'message': response.json()['cause'][0]['description']}, status=response.status_code)
  return render(request, 'orders/create_customer.html')


def search_customer(request):
  print(MERCADOPAGO_TEST_ACCESS_TOKEN)
  email = 'customer@example.com'
  url = f'https://api.mercadopago.com/v1/customers/search?email={email}'
  resp = requests.get(url, headers={
      "Authorization": "Bearer " + MERCADOPAGO_TEST_ACCESS_TOKEN})
  resp = resp.json()

  return JsonResponse({'customer': resp})


def get_customer(request):
  return JsonResponse({'customer': 'customer'})


def get_customer(request):
  print(MERCADOPAGO_TEST_ACCESS_TOKEN)
  email = 'customer@example.com'
  url = f'https://api.mercadopago.com/v1/customers/search?email={email}'
  resp = requests.get(url, headers={
      "Authorization": "Bearer " + MERCADOPAGO_TEST_ACCESS_TOKEN})
  resp = resp.json()

  return JsonResponse({'customer': resp})


def get_customer(request):
  return JsonResponse({'customer': 'customer'})
