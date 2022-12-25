from django.contrib import admin
from django.urls import path, include
from .views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='Home-page'),
    path('', include('todoapi.urls')),
    path('', include('Notesapi.urls')),
    path('', include('authapi.urls')),
]
