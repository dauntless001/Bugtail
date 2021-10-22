from django.urls import path
from accounts import views

app_name='accounts'

urlpatterns = [
    path('edit-account/', views.ChangeUserDetailsView.as_view(), name='edit_account'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
]