from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse ("congratulations you have created a web application using django")
def home (request):
    return render(request, 'home.html')
# Create your views here.
