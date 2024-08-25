# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def list(req):
     return render (req,'track/list.html')

def update(req):
     return render (req,'track/update.html')

def delete(req):
     return render (req,'track/delete.html')
def show_details(req):
     return render (req,'track/showDetails.html')
def create(req):
     return render (req,'track/create.html')


