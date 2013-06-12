from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now=True)
    job_title = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    review_type = models.CharField(max_length=50, blank=False, null=False)
    company = models.CharField(max_length=100, blank=False, null=False)
    overall_experience = models.IntegerField()
    comments = models.TextField()

