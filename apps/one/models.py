from django.db import models

# Create your models here.

class Event(models.Model):
    service = models.CharField(max_length=255, default="", null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    response_time = models.DateTimeField(null=True, blank=True)
    path = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    request = models.JSONField(default=dict)
    response = models.JSONField(default=dict)
    response_code = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.service

    class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"