from django.urls import path
from django.views import View
from .views import *

urlpatterns = [
    path ('',IndexView.as_view(),name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('home/',HomeView.as_view(),name='home'),
    path('register/',RegistView.as_view(),name='register')

]