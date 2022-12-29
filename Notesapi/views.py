# Importing Response from rest framework.
from rest_framework.response import Response
# Importing Api View from rest framework.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# Importing note serializer from serializers file
from Notesapi.serializers import NoteSerializer
# Importing Note table from models.
from Notesapi.models import Note
from rest_framework.permissions import IsAuthenticated

# List View class 
class NoteListView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        notes = Note.objects.filter(user=user)
        return notes

# Create View class
class NoteCreateView(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        notes = Note.objects.filter(user=user)
        return notes


# Retrive View class
class NoteRetrieveView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        notes = Note.objects.filter(user=user)
        return notes

# Update View class
class NoteUpdateView(UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        notes = Note.objects.filter(user=user)
        return notes

# Delete View class
class NoteDestroyView(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        notes = Note.objects.filter(user=user)
        return notes
