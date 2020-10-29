import datetime

# from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone

# Create your models here.
# class Example(models.Model):
#   example_text = models.CharField(max_length=200)
#   pub_date = models.DateTimeField('date published')

#   def __str__(self):
#     return self.example_text
#   def was_published_recently(self):
#     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Question(models.Model):
  question_name = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  data = models.CharField(max_length=200)

  def __str__(self):
    return self.question_name
    return self.data
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
