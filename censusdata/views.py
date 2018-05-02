from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    mycontext = {
        'message': 'Enter your address'
    }
    return render(request, 'censusdata/mainform.html', mycontext)
