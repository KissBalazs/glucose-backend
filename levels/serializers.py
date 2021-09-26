from rest_framework import serializers
from django.contrib.auth.models import User
from levels.models import Level

class LevelSerializer(serializers.ModelSerializer):
    """
    Basic serializer to handle the Glucose Levels. using the built in ModelSerializes.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Level
        fields = ['id', 'title', 'description', 'owner']


class UserSerializer(serializers.ModelSerializer):
    """
    Built in serializer, to be able to retrieve Glucose Levels for users.
    """
    levels = serializers.PrimaryKeyRelatedField(many=True, queryset=Level.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'levels']
