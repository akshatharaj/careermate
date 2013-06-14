from django.db import models
from django.contrib.auth.models import User

REVIEW_TYPE_CHOICES = [
    ('Job Interview', u'Job Interview'),
    ('Employer/Company', u'Employer/Company'),
]

OVERALL_EXPERIENCE_CHOICES = [
    ('Overall Negative', u'Overall Negative'),
    ('Overall Neutral', u'Overall Neutral'),
    ('Overall Positive', u'Overall Positive'),
]

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

