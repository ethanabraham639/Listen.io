#serializers.py takes the python code from models.py and converts it to a JSON (JavaScript
#Object Notation) response. The serializer makes sure that the requests from the client
#are valid by making sure that the fields match

from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')

class UpdateRoomSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[])
    
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip', 'code')