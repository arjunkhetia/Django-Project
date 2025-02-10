from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user(request):
    return HttpResponse("User works.")

def user_by_id(request, id):
    return HttpResponse(f'User by id : {id} works.')