from django.db import models

class TodoModel(models.Model):
    title = models.CharField(max_length=222)
    description = models.CharField(max_length=1000)
    isCompleted = models.BooleanField()


