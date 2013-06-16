from django.db import models
from django.contrib.auth.models import User

from constants import REVIEW_TYPE_CHOICES, OVERALL_EXPERIENCE_CHOICES

class Post(models.Model):
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now=True)
    job_title = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    review_type = models.CharField(max_length=50, blank=False, null=False, 
                                   choices=REVIEW_TYPE_CHOICES)
    company = models.CharField(max_length=100, blank=False, null=False)
    overall_experience = models.CharField(max_length=50, blank=True, null=True, 
                                          choices=OVERALL_EXPERIENCE_CHOICES)
    comments = models.TextField()
    is_live = models.BooleanField(default=True)

class PostReport(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    created = models.DateTimeField(auto_now=True)
    reason = models.TextField()


class PostResponse(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    created = models.DateTimeField(auto_now=True)
    comments = models.TextField()
    email_follow_up = models.BooleanField(default=False)
