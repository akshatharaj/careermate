from collections import defaultdict

from django.db.models import Q
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from models import PostReport

def notify_all_response_listeners(post_response):
    """
    given a response object, this method emails all other earlier responders 
    on the same post who chose to be notified when a new response is submitted
    """

    post = post_response.post
    listeners = post.postresponse_set.filter(~(Q(author=post_response.author)),
                                             created__lt=post_response.created,
                                             email_follow_up=True)
    listeners = map(lambda x: x.author.email, listeners)
    if listeners:
        email_subject = 'New comment received on the review you subscribed to on Careermate'
        body_template = 'cmapp/email_template/new_response_notice.html'
        send_mail(email_subject, render_to_string(body_template, {'post': post}),
                  settings.SERVER_EMAIL, listeners, fail_silently=True)



def accept_post_reports(report_queryset):
    impacted_posts = map(lambda x: x.post, report_queryset)
    for post in impacted_posts:
        post.is_live = False
        post.save()
        PostReport.objects.filter(post=post).delete()    
