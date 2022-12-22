# Importing path from django urls.
from django.urls import path
# Importing views from Views.
from todoapi.views import TaskListView, TaskCreateView, TaskRetrieveView, TaskUpdateView, TaskDestroyView


urlpatterns = [
    path('api/tasks/', TaskListView.as_view()),
    path('api/tasks/create/', TaskCreateView.as_view()),
    path('api/tasks/update/<str:pk>/', TaskUpdateView.as_view()),
    path('api/tasks/delete/<str:pk>/', TaskDestroyView.as_view()),
    path('api/tasks/<str:pk>/', TaskRetrieveView.as_view()),
]