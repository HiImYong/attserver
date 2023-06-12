import json
from django.http import HttpResponse
import requests
from django.shortcuts import render

# Create your views here.

def hello(request) : 
    print('hello!')
    result = '{"test": "good"}'
    response = HttpResponse(result, content_type='application/json')
    return response