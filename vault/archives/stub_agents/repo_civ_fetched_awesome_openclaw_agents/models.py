from django.db import models

class DataModel(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    def __str__(self):
        return f'{self.timestamp} - {self.value}'