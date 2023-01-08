from django.db import models
import datetime
class Task(models.Model):
    def __str__(self):
        return self.task
    task=models.CharField(max_length=200)
    priority=models.IntegerField()
    date=models.DateField(default=datetime.date.today)

# Create your models here.
