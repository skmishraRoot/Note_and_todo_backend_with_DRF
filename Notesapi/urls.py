# Importing path from django urls.
from django.urls import path
# Importing views from Views.
from Notesapi.views import NoteListView, NoteCreateView, NoteRetrieveView, NoteUpdateView, NoteDestroyView


urlpatterns = [
    path('api/Notes/', NoteListView.as_view()),
    path('api/Notes/create/', NoteCreateView.as_view()),
    path('api/Notes/update/<str:pk>/', NoteUpdateView.as_view()),
    path('api/Notes/delete/<str:pk>/', NoteDestroyView.as_view()),
    path('api/Notes/<str:pk>/', NoteRetrieveView.as_view()),
]