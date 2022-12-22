# Importing model serializer
from rest_framework.serializers import ModelSerializer
# Importing Notes table from Notesapp
from todoapi.models import Task


# Defining serializer for Task table
class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"