from django.urls import path
from notifications import views

app_name = 'notifications'

urlpatterns = [
    path('mark-all-as-read/', views.MarkNotifications.as_view(), name='mark_all_as_read'),
]