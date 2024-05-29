from django.urls import path
from payments import views

urlpatterns = [

    # WEB
    path('payments/', views.payments, name='payments'),
    path('create_customer/', views.create_customer, name='create_customer'),

    # API

]
