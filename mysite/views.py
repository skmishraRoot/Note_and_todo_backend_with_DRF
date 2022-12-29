from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def Home(request):
    routes = {
        'Todo_app':"/api/todo = Todo application api",
        'Notes_app':"/api/Notes = Note application api",
        'accounts':"/register = auth register api"
    }
    return  Response(routes)