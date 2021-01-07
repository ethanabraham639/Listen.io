#urls.py in spotify/ is used to redirect the user to authenticate themselves (sign in)
#from spotify.com and once they have done that the spotify_callback will redirect them
#back to the frontend (their room in Listen.io)

from django.urls import path
from .views import AuthURL, spotify_callback, IsAuthenticated

urlpatterns = [
    path('get-auth-url', AuthURL.as_view()),
    path('redirect', spotify_callback),
    path('is-authenticated', IsAuthenticated.as_view())
]