import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
#from django.http import JsonResponse
import json


# Create your views here.
def trending_lang(request):
    time_now = datetime.now()
    last_month = (time_now - timedelta(days=30)).strftime("%Y-%m-%d")
    url = "https://api.github.com/search/repositories?q=created:>{0}&sort=stars&order=desc&page=1&per_page=100".format(last_month)
    data=requests.get(url).json()

    set_of_lang = {element['language'] for element in data['items'] if element['language'] != None}
    
    return HttpResponse(json.dumps(data), content_type="application/json")