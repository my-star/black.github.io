from django.urls import path
from . import views

urlpatterns = [
    path('pub_list/', views.publisher_list),
    path('<int:id>/', views.edit_publisher, name="edit_publisher"),
    path('add_publisher/', views.add_publisher, name="add_publisher")
]