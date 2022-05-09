import requests
from django.http import HttpResponse

def myhome(request):
    return HttpResponse("Hello, world. You're at the myhome page.")