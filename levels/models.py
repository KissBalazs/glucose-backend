from django.db import models


class Level(models.Model):
    """
    The default model to store the Glucose level data.
    """

    start = models.DateTimeField(auto_now_add=True)
    stop = models.DateTimeField(auto_now_add=True)
    gerat = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey(
        'auth.User', related_name='levels', on_delete=models.CASCADE)

    class Meta:
        ordering = ['start']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
