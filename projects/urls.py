from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('-/new/', views.ProjectCreateView.as_view(), name='project_create'),
    path('<str:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('<str:slug>/-/issue/', views.CreateIssueView.as_view(), name='create_issue'),
    path('<str:slug>/-/issue/<str:issue_slug>/', views.IssueView.as_view(), name='issue_detail'),
    path('<str:slug>/add-collaborators/', views.AddRemoveCollaboratorView.as_view(), name='add_remove_collaborator'),
    path('-/assign/', views.assign_task, name='assign_task'),
    path('<str:slug>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('<str:slug>/edit/', views.ProjectEditView.as_view(), name='project_edit'),
    path('<str:slug>/settings/', views.ProjectSettingsView.as_view(), name='project_settings'),
]