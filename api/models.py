#models.py in api/ is used to declare the structure of each thing in the program
#here we have a class for Room which declares the structure for a Room

#django uses this structure to store information in a database format so that we
#are able to access specific information about a Room in an organized way

#django REST framework is being used to build a Web API so that we can see the
#HTTP requests and responses that are being made for different actions

from django.db import models
import string
import random


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code


class Room(models.Model):
    code = models.CharField(
        max_length=8, default=generate_unique_code, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)