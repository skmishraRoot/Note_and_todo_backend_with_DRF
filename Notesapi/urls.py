# Importing path from django urls.
from django.urls import path
# Importing views from Views.
from Notesapi.views import NoteListView, NoteCreateView, NoteRetrieveView, NoteUpdateView, NoteDestroyView


urlpatterns = [
    path('api/notes/', NoteListView.as_view()),
    path('api/notes/create/', NoteCreateView.as_view()),
    path('api/notes/update/<str:pk>/', NoteUpdateView.as_view()),
    path('api/notes/delete/<str:pk>/', NoteDestroyView.as_view()),
    path('api/notes/<str:pk>/', NoteRetrieveView.as_view()),
]