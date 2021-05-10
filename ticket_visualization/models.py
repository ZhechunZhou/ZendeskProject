from django.db import models


class Ticket(models.Model):
    id = models.IntegerField(primary_key=True)
    assignee_id = models.IntegerField(default=None)
    created_at = models.DateTimeField()
    description = models.CharField(max_length=200, default=None)
    due_at = models.DateTimeField(default=None)
    priority = models.CharField(max_length=20, default=None)
    status = models.CharField(max_length=20, default=None)
    subject = models.CharField(max_length=200, default=None)
    submitter_id = models.IntegerField(default=None)
    type = models.CharField(max_length=20, default=None)
    updated_at = models.DateTimeField(default=None)
    url = models.URLField(max_length=200)
