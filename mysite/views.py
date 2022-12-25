from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def Home(request):
    routes = {
        'Todo_app':"/api/tasks",
        'Notes_app':"/api/Notes",
        'accounts':"/register"
    }
    return  Response(routes)