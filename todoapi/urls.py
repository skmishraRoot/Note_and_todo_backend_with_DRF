# Importing path from django urls.
from django.urls import path
# Importing views from Views.
from todoapi.views import TaskListView, TaskCreateView, TaskRetrieveView, TaskUpdateView, TaskDestroyView


urlpatterns = [
    path('api/todo/', TaskListView.as_view()),
    path('api/todo/create/', TaskCreateView.as_view()),
    path('api/todo/update/<str:pk>/', TaskUpdateView.as_view()),
    path('api/todo/delete/<str:pk>/', TaskDestroyView.as_view()),
    path('api/todo/<str:pk>/', TaskRetrieveView.as_view()),
]