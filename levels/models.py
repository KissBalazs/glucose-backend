from django.db import models


class Level(models.Model):
    """
    The default model to store the Glucose level data.
    """

    start = models.DateTimeField(auto_now_add=True)
    stop = models.DateTimeField(auto_now_add=True)
    gerat = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['start']
