from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    last_picked = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title