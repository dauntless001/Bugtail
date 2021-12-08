from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('-/new/', views.ProjectCreateView.as_view(), name='project_create'),
    path('<str:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('-/assign/', views.assign_task, name='assign_task'),
    path('<str:slug>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('<str:slug>/edit/', views.ProjectEditView.as_view(), name='project_edit'),
    path('<str:slug>/settings/', views.ProjectSettingsView.as_view(), name='project_settings'),
]