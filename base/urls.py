from django.urls import path
from base import views

app_name = 'base'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),

]
