from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
import requests
from bs4 import BeautifulSoup
# Create your views here.

def home(request):
    t=loader.get_template('home.html')
    res = requests.get('http://jandan.net/ooxx/page-1966#comments')
    html = BeautifulSoup(res.text,'lxml')
    pic_indexs=[]
    for index in html.select('#comments img'):
        pic_indexs.append(index.get('src'))
    c=Context({'pic_indexs':pic_indexs})
    return HttpResponse(t.render(c))