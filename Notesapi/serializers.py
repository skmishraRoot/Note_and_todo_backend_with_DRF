# Importing model serializer
from rest_framework.serializers import ModelSerializer
# Importing Notes table from Notesapp
from Notesapi.models import Note


# Defining serializer for Note table
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"