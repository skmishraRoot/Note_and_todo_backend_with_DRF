# Importing Response from rest framework.
from rest_framework.response import Response
# Importing Api View from rest framework.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# Importing note serializer from serializers file
from todoapi.serializers import TaskSerializer
# Importing task table from models.
from todoapi.models import Task
from rest_framework.permissions import IsAuthenticated


# List View class
class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        notes = Note.objects.filter(user=user)
        return notes


    
# Create View class
class TaskCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        notes = Note.objects.filter(user=user)
        return notes



# Retrive View class
class TaskRetrieveView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        notes = Note.objects.filter(user=user)
        return notes



# Update View class
class TaskUpdateView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        notes = Note.objects.filter(user=user)
        return notes



# Delete View class
class TaskDestroyView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        notes = Note.objects.filter(user=user)
        return notes
