from django.db import models


class Ticket(models.Model):
    id = models.IntegerField(primary_key=True)
    assignee_id = models.IntegerField(null=True, default=None)
    submitter_id = models.IntegerField(null=True, default=None)
    requester_id = models.IntegerField(null=True, default=None)
    created_at = models.DateTimeField()
    description = models.CharField(max_length=200, null=True, default=None)
    due_at = models.DateTimeField(null=True, default=None)
    priority = models.CharField(max_length=20, null=True, default=None)
    status = models.CharField(max_length=20, null=True, default=None)
    subject = models.CharField(max_length=200, null=True, default=None)
    type = models.CharField(max_length=20, null=True, default=None)
    updated_at = models.DateTimeField(null=True, default=None)
    url = models.URLField(max_length=200)
