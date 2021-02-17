#urls.py in the api folder is to set a path for the different endpoints to access the
#different APIViews made in view.py. At each of the api endpoints we will be requesting
#information from the backend and sending back HTTP responses indicating what action was done

from django.urls import path
from .views import RoomView, CreateRoomView, GetRoom, JoinRoom, UserInRoom, LeaveRoom, UpdateRoom

urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
    path('user-in-room', UserInRoom.as_view()),
    path('leave-room', LeaveRoom.as_view()),
    path('update-room', UpdateRoom.as_view())
]