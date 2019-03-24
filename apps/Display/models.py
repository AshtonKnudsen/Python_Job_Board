from __future__ import unicode_literals
from django.db import models
from apps.LoginReg.models import User

class Job_manager(models.Manager):
    def Job_validator(self, postData):
        errors = {}
        if len(postData["title"]) < 3:
            errors["title"] = "Title must be at least 3 characters"
        if len(postData["location"]) < 5:
            errors["location"] = "Location must be longer"
        if len(postData["description"]) < 10:
            errors["description"] = "How are they going to know what to do if you dont describe the job?"
        return errors

class Job(models.Model):
    user = models.ForeignKey(User, related_name="jobs")
    job_title = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = Job_manager()

