from django.db import models
import datetime

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    deadline = models.DateField()

    def __str__(self):
        return self.title

    def get_date(self):
        return str(self.deadline)

    def time_left(self):
        current_date = datetime.date.today()
        delta = self.deadline - current_date
        return delta.days
