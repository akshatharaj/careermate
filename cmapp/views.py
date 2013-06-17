from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django import forms as django_forms
from django.db.models import Q

from forms import PostForm, PostReportForm, PostSearchForm, PostResponseForm
from constants import POST_ADD_SUGGESTION, REPORT_POST_SUGGESTION, POST_RESPONSE_SUGGESTION
from models import Post, PostResponse
from utils import notify_all_response_listeners

def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


def login_user(request):
    state = "Please log in below..."
    username = password = ''
    context = {'state': state}
    context.update(csrf(request))

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        context['username'] = username

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context['state'] = "You're successfully logged in!"
                return redirect('home')                
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('auth.html', context)


def add_new_post(request):
    author = User.objects.get(pk=request.user.id)
    if request.method == 'GET':
        form = PostForm()
        form.fields['author'].widget = django_forms.HiddenInput()
        form.fields['author'].initial = author
        form.fields['is_live'].widget = django_forms.HiddenInput()
        form.fields['is_live'].initial = 'on'
        return render_to_response('cmapp/post/change_form.html', 
                           {'form': form, 'suggest_text': POST_ADD_SUGGESTION},
                           RequestContext(request))

    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form.fields['is_live'].widget = django_forms.HiddenInput()
            form.fields['author'].widget = django_forms.HiddenInput()
            return render_to_response('cmapp/post/change_form.html',
                                      {'errors': form.errors, 'form': form,
                                       'suggest_text': POST_ADD_SUGGESTION},
                                      RequestContext(request))
        return redirect('home')


def list_posts(request):
    if request.method == 'GET':
        search_form = PostSearchForm()
        posts = Post.objects.filter(is_live=True)
        search_text = request.GET.get('search_text', None)
        if search_text:
            posts = posts.filter(Q(job_title__icontains=search_text) |
                                 Q(city__icontains=search_text) |
                                 Q(company__icontains=search_text))
        posts = posts.order_by('created')
        return render_to_response('cmapp/post/list.html', {'posts': posts,
                                   'search_form': search_form}, RequestContext(request))

def report_post(request, **kwargs):
    post_id = kwargs.get('post_id', request.REQUEST.get('post'))
    post = Post.objects.get(pk=post_id)
    author = User.objects.get(pk=request.user.id)
    if request.method == 'GET':
        form = PostReportForm()
        form.fields['author'].widget = django_forms.HiddenInput()
        form.fields['author'].initial = author
        form.fields['post'].widget = django_forms.HiddenInput()
        form.fields['post'].initial = post
        return render_to_response('cmapp/postreport/change_form.html',
                           {'form': form, 'suggest_text': REPORT_POST_SUGGESTION,
                            'post': post},
                           RequestContext(request))

    if request.method == 'POST':
        post = None
        form = PostReportForm(request.POST)
        if form.is_valid():
            post = form.cleaned_data.get('post')
            form.save()
            messages.add_message(request, messages.INFO, 'Your report has been accepted.')
        else:
            form.fields['post'].widget = django_forms.HiddenInput()
            form.fields['author'].widget = django_forms.HiddenInput()
            return render_to_response('cmapp/postreport/change_form.html',
                                      {'errors': form.errors, 'form': form,
                                       'post': form.cleaned_data.get('post'), 
                                       'suggest_text': REPORT_POST_SUGGESTION},
                                      RequestContext(request))
        return redirect(reverse('post-detail', kwargs={'post_id': post.id}))

def respond_to_post(request, **kwargs):
    post_id = kwargs.get('post_id', request.REQUEST.get('post'))
    post = Post.objects.get(pk=post_id)
    author = User.objects.get(pk=request.user.id)
    if request.method == 'GET':
        form = PostResponseForm()
        form.fields['author'].widget = django_forms.HiddenInput()
        form.fields['author'].initial = author
        form.fields['post'].widget = django_forms.HiddenInput()
        form.fields['post'].initial = post
        form.fields['email_follow_up'].label = 'Email me when other users comment on this post'
        return render_to_response('cmapp/postresponse/change_form.html',
                           {'form': form, 'suggest_text': POST_RESPONSE_SUGGESTION,
                            'post': post},
                           RequestContext(request))

    if request.method == 'POST':
        post = None
        form = PostResponseForm(request.POST)
        if form.is_valid():
            post = form.cleaned_data.get('post')
            response = form.save()
            notify_all_response_listeners(response)
            messages.add_message(request, messages.INFO, 'Response submission successful!')
        else:
            form.fields['post'].widget = django_forms.HiddenInput()
            form.fields['author'].widget = django_forms.HiddenInput()
            form.fields['email_follow_up'].label = 'Email me when other users comment on this post'
            return render_to_response('cmapp/postresponse/change_form.html',
                                      {'errors': form.errors, 'form': form, 
                                       'suggest_text': POST_RESPONSE_SUGGESTION,
                                       'post': form.cleaned_data.get('post')},        
                                      RequestContext(request))
        return redirect(reverse('post-detail', kwargs={'post_id': post.id}))

def post_detail(request, **kwargs):
    post_id = kwargs.get('post_id', request.REQUEST.get('post'))
    post = Post.objects.get(pk=post_id)
    responses = post.postresponse_set.all().order_by('-created')
    if request.method == 'GET':
        return render_to_response('cmapp/post/detail.html',
                           {'post': post, 'post_responses': responses},
                           RequestContext(request))
