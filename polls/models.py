import datetime

from django.db import models
from django.utils import timezone

class Invention(models.Model):
    invention_name = models.CharField(max_length=50)
    publication_date = models.DateTimeField("Publish date")

    def __str__(self) -> str:
        return self.invention_name

    def was_published_recentrly(self):
        return self.publication_date >= timezone.now() - datetime.timedelta(days=1)

class Proposal(models.Model):
    invention = models.ForeignKey(Invention, on_delete=models.CASCADE)
    proposed_sum = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)