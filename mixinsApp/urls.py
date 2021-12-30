from django.urls import path
from mixinsApp import views

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view()),
    path('employees/<int:pk>', views.EmployeeDetailView.as_view()),
]