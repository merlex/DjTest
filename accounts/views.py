from django.contrib import auth
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
#from django import forms
#from django.http import HttpResponseRedirect
#from django.contrib.auth.forms import UserCreationForm

#def register(request):
#    form = UserCreationForm()
#
#    if request.method == 'POST':
#        data = request.POST.copy()
#        errors = form.get_validation_errors(data)
#        if not errors:
#            new_user = form.save(data)
#            return HttpResponseRedirect("/blog/")
#    else:
#        data, errors = {}, {}
#
#    return render_to_response("accounts/register.html", {
#        'form' : form,
#    })

def login(request, **kw):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/accounts/loggedin/")
        else:
            return HttpResponseRedirect("/accounts/invalid/")
    else:
        context = RequestContext(request, kw)
        return render_to_response("accounts/login.html", context)

def logout(request, **kw):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/loggedout/")
def loggedin(request, **kw):
    if request.user.is_authenticated():
        context = RequestContext(request, kw)
        return render_to_response("accounts/account.html", context)
    else:
        return HttpResponseRedirect("/account/login/")

