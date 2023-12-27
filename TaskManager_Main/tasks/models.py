from django.db import models


# Create your models here.

class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"


class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    description = models.CharField(verbose_name="Task Description", max_length=255, unique=True)
    due_date =models.DateField(verbose_name="Task Due Date", max_length=65, )
    status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices)

    def __str__(self):
        return self.name
