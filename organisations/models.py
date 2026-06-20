from django.db import models
from django.conf import settings


class Organisation(models.Model):
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='managed_organisations')
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_email = models.EmailField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name