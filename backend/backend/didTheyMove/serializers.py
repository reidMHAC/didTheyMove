from rest_framework import serializers
from .models import DidTheyMove

class DidTheyMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = DidTheyMove
        fields = ('id', 'customer', 'address', 'zipCode', 'phoneNumber', 'status')

class CheckMovedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DidTheyMove
        fields = ['client']