from django.urls import path
from .views import SignUpView, ProfileView , ChangeView
urlpatterns=[
    path('signup/',SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/',ProfileView.as_view(), name='profile'),
    path('change/<int:pk>/',ChangeView.as_view(), name='change'),
    
] 