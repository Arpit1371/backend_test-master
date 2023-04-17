from django.urls import path

from main import views

app_name = 'api'

urlpatterns = [
    path('', views.companies_view),
    path('add_employee/<str:company_name>/', views.add_employee, name='add_employee'),
]
