from django.urls import path
from accounts import views

urlpatterns = [

    # WEB
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),

    # API

]
