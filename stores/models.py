from django.db import models
from django.conf import settings

class Store(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Stores')
    name = models.CharField(max_length=20, blank=True, null=True)
    gst_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

def __str__(self):
    return f"{self.name} - {self.owner.username}"