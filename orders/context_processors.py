from django.conf import settings


def get_mercadopago_test_access_token(request):
  return {'MERCADOPAGO_TEST_ACCESS_TOKEN': settings.MERCADOPAGO_TEST_ACCESS_TOKEN}
