# PYTHON IMPORTS
import os
import uuid
import json
from datetime import datetime

# DJANGO IMPORTS
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

#External Lib 
from dotenv import load_dotenv # pip i python-dotenv
import requests
from bs4 import BeautifulSoup

# External files
from .fox import scraper

# Create your views here.
@csrf_exempt
def index(request):
  body_unicode = request.body.decode('utf-8')
  body = json.loads(body_unicode)
  url = body['url']
  allText = scraper(url)
  print("\n", allText, "\n")
  apiResponse = {
      "Status": 200
    }
  return JsonResponse(apiResponse)