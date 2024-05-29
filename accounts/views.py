from django.shortcuts import render

# Create your views here.


def signin(request):
  return render(request, 'accounts/signin.html')


def signup(request):
  # print(request.META.keys())
  print(request.META.values())
  if request.META.get('HTTP_ACCEPT'):
    print(request.META.get('HTTP_ACCEPT'))
    return render(request, 'accounts/signup.html')

  else:
    print('São Jorge')
  # if request.META.get('CONTENT_TYPE', 'application/json'):
  #   print(request.META.get('CONTENT_TYPE', 'application/json'))
  #   print('Por Aqui')
  #   return Response({'msg': 'Deu Certo'})
