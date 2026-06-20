from django.db import models
from organisations.models import Organisation


class Event(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'), ('ms', 'Malay'),
        ('zh', 'Mandarin'), ('ta', 'Tamil'), ('any', 'Any'),
    ]
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=300)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    language_requirement = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='any')
    max_volunteers = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title