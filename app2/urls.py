from django.urls import path
from .views import index,login

urlpatterns = [
    path('login/',login),
    path('',index)
]