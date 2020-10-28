from django.db import models

# Create your models here.
class Example(models.Model):
  example_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')