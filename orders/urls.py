from django.urls import path
from orders import views


urlpatterns = [
    path('create_customer/', views.create_customer, name='create_customer'),
    path('search_customer/', views.search_customer, name='search_customer'),
    path('get_customer/', views.get_customer, name='get_customer'),
]
