from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django import forms as django_forms
from django.db.models import Q

from forms import PostForm, PostReportForm, PostSearchForm
from constants import POST_ADD_SUGGESTION, REPORT_POST_SUGGESTION
from models import Post

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
    if request.method == 'GET':
        form = PostForm()
        form.fields['author'].widget = django_forms.HiddenInput()
        form.fields['is_live'].widget = django_forms.HiddenInput()
        return render_to_response('admin/cmapp/post/change_form.html', 
                           {'form': form, 'suggest_text': POST_ADD_SUGGESTION},
                           RequestContext(request))

    if request.POST:
        post_data = request.POST.copy()
        post_data['author'] = request.user.id
        post_data['is_live'] = True
        form = PostForm(post_data)
        form.fields['author'].widget = django_forms.HiddenInput()
        form.fields['is_live'].widget = django_forms.HiddenInput()
        context = {'suggest_text': POST_ADD_SUGGESTION}
        context.update(csrf(request))
        if not form.is_valid():
            context['form'] = form
            return render_to_response('admin/cmapp/post/change_form.html', context,
                                       RequestContext(request))
        post = form.save()
        return redirect('home')


def list_posts(request):
    if request.method == 'GET':
        search_form = PostSearchForm()
        posts = Post.objects.filter(is_live=True)
        if request.GET.get('q', None):
            posts = posts.filter(Q(job_title__icontains=q) |
                                 Q(city__icontains=q) |
                                 Q(company__icontains=q))
        posts = posts.order_by('created')
        return render_to_response('admin/cmapp/post/list.html', {'posts': posts,
                                   'search_form': search_form}, RequestContext(request))

def report_post(request, **kwargs):
    post_id = kwargs.get('post_id')
    post = Post.objects.get(pk=post_id)
    if request.method == 'GET':
        form = PostReportForm()
        form.fields['author'].widget = django_forms.HiddenInput()
        form.fields['post'].widget = django_forms.HiddenInput()
        return render_to_response('admin/cmapp/reportpost/change_form.html',
                           {'form': form, 'suggest_text': REPORT_POST_SUGGESTION,
                            'post': post},
                           RequestContext(request))

    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['author'] = request.user.id
        post_data['post'] = post.id
        post = form.save()
        return redirect('home')
        return render_to_response('admin/cmapp/post/list.html', {'posts': posts},
                                   RequestContext(request))
