from django.http import HttpResponse
from django.shortcuts import redirect

'''
Decorator is a function that takes in another function as a parameter
an lets us add extra functionality before the original function is called
'''
#viewfunc here is the view function
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        #if user is authenticated redirect it to home page
        if request.user.is_authenticated:
            return redirect('home')
        #else return to view func which in this case is login page
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    # here view func is all the other function which are restricted to other roles 
    # except admin
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            # check if user is part of the group then set the 
            # first value of group to the variable
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            # if group is in the list of allowed roles then return the view func
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            # else return the http response 
            else:
                return HttpResponse('You are not authorized to view this page')

        return wrapper_func

    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        # if group is customer then redirect to user page
        if group == 'customer':
            return redirect('user-page')
        # if group is admin return vieww func
        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function
