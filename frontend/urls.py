#urls.py in frontend are the urls that the user will actually see
#Each of those paths is a different page for the user

from django.urls import path
from .views import index

app_name = 'frontend'

urlpatterns = [
    path('', index, name=''),
    path('join', index),
    path('create', index),
    path('room/<str:roomCode>', index)
]