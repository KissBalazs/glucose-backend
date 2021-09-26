from django.contrib.auth.models import User
from rest_framework import serializers

from levels.models import Level


class LevelSerializer(serializers.ModelSerializer):
    """
    Basic serializer to handle the Glucose Levels. using the built in ModelSerializes.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Level
        fields = ['id', 'start', 'stop', 'gerat', 'seriennummer', 'geratezeitstempel', 'owner']


class UserSerializer(serializers.ModelSerializer):
    """
    Built in serializer, to be able to retrieve Glucose Levels for users.
    """
    levels = serializers.PrimaryKeyRelatedField(many=True, queryset=Level.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'levels']
