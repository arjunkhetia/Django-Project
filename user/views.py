from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user(request):
    return HttpResponse("User works.")

def userid_int(request, id):
    return HttpResponse(f'User by id : {id} works. ID is Integer')

def userid_str(request, id):
    return HttpResponse(f'User by id : {id} works. ID is String')

def userid_uuid(request, id):
    return HttpResponse(f'User by id : {id} works. ID is UUID')