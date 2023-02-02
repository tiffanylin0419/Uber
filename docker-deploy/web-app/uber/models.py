from django.db import models

# Create your models here.
import datetime
from django.utils import timezone


class RequestRide(models.Model):
    address = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.address
    #def was_published_recently(self):
    #    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        