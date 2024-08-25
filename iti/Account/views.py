from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list(req):
    return render (req,'account/list.html')

def update(req):
    return render (req,'account/update.html')

def delete(req):
    return render (req,'account/delete.html')
def show_details(req):
    return render (req,'account/showDetails.html')
def create(req):
    return render (req,'account/create.html')



