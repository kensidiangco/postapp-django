from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def unauthenticated_user(view_func):
    def wrapper(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('post'))
        else:
            return view_func(request, *args, **kwargs)
    return wrapper
        
        
def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'user':
            return HttpResponseRedirect(reverse('post'))
            
        elif group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper