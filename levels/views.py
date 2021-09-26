# Create your views here.
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets

from levels.models import Level
from levels.serializers import LevelSerializer, UserSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    # authentication_classes = (TokenAuthentication,)  todo: enable token authentication to be more secure (or session maybe)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
