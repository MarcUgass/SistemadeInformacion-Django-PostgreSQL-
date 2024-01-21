from django.test import TestCase
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
