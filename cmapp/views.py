from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.shortcuts import redirect

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
