from django.db import models
class Knowledge(models.Model):
    user_id = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)