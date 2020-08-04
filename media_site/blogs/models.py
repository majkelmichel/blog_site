from django.db import models
import datetime

# Create your models here.


class Submission(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now())

    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username
