from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeEmployers.as_view(), name='employer'),
]