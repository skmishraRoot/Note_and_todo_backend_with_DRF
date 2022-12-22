# Importing Response from rest framework.
from rest_framework.response import Response
# Importing Api View from rest framework.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# Importing note serializer from serializers file
from Notesapi.serializers import NoteSerializer
# Importing Note table from models.
from Notesapi.models import Note


# List View class
class NoteListView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# Create View class
class NoteCreateView(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# Retrive View class
class NoteRetrieveView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# Update View class
class NoteUpdateView(UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# Delete View class
class NoteDestroyView(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
