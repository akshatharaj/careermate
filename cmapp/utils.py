from django.db.models import Q
from django.core.mail import send_mail

def notify_all_response_listeners(post_response):
    """
    given a response object, this method emails all other earlier responders 
    on the same post who chose to be notified when a new response is submitted
    """
    post = post_response.post
    listeners = post.postresponse_set.filter(~(Q(id=post_response.id)), 
                                             created__lt=post_response.created,
                                             email_follow_up=True)
    listeners = map(lambda x: x.author.email, listeners)
    if listeners:
        email_subject = 'New comment received on the review you subscribed to on Careermate'
        body_template = 'cmapp/email_template/new_response_notice.html'
        send_mail(email_subject, render_to_string(body_template, {'post': post}),
                  settings.SERVER_EMAIL, listeners, fail_silently=True)




