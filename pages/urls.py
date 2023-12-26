from django.urls import path
from .views import esasysahypa
urlpatterns=[
    path('',esasysahypa.as_view(),name='home'),
]