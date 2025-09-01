from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
import datetime
# Create your models here.

class Meeting(models.Model):
    title = models.CharField(("Title"), max_length=200)
    start_time = models.DateTimeField(("Start Time"))
    end_time = models.DateTimeField(("End Time"))
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='meetings')
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='organized_meetings', on_delete=models.CASCADE)
    
    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")

        conflict = Meeting.objects.filter(
            participants__in=self.participants.all(),
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        
        ).exclude(pk=self.pk)

        if conflict.exists():
            raise ValidationError("Meeting conflicts with existing meetings.")


        def __str__(self):
            return self.title

        