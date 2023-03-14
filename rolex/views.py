from django.shortcuts import render
from django.http import HttpResponse

def dilli(request):
 return HttpResponse('<h1>my name is dilli</h1>')
