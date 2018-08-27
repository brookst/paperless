from django.db import models


class Reminder(models.Model):

    document = models.ForeignKey("documents.Document", models.PROTECT)
    date = models.DateTimeField()
    note = models.TextField(blank=True)
