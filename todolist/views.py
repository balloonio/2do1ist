from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.
def index(request):
    message = "Current Time: {}".format(datetime.datetime.now())
    return HttpResponse(message)