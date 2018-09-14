from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateField('date published', auto_now=True)

    def __str__(self):
        return self.text
