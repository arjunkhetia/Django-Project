from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def user(request):
    return HttpResponse("User works.")

def userid_int(request, id):
    if id == 404:
        return HttpResponseNotFound('404 ID is not allowed')
    else :
        return HttpResponse(f'User by id : {id} works. ID is Integer')

def userid_str(request, id):
    return HttpResponse(f'User by id : {id} works. ID is String')

def userid_uuid(request, id):
    return HttpResponse(f'User by id : {id} works. ID is UUID')

def user_home(request):
    return render(request, 'user/home.html')

def user_user(request):
    return render(request, 'user/user.html', {
        'user': 'Arjun'
    })