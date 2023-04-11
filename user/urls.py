from django.urls import path
from user.views import RegisterUserApi,LoginApi

urlpatterns = [
  path('',RegisterUserApi.as_view(),name='Register'),
  path('login/',LoginApi.as_view(),name='Login')
]