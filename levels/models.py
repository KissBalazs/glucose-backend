from django.db import models
from rest_framework.authentication import TokenAuthentication


class Level(models.Model):
    """
    The default model to store the Glucose level data.
    """
    start = models.DateTimeField(auto_now_add=True)
    stop = models.DateTimeField(auto_now_add=True)
    gerat = models.CharField(max_length=100, blank=True, default='')
    seriennummer = models.CharField(max_length=100, blank=True, default='')
    geratezeitstempel = models.CharField(max_length=100, blank=True, default='')
    authentication_classes = (TokenAuthentication,)
    owner = models.ForeignKey(
        'auth.User', related_name='levels', on_delete=models.CASCADE)

    class Meta:
        ordering = ['start']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
