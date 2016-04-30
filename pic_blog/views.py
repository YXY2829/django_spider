from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
import requests
from bs4 import BeautifulSoup
import time
# Create your views here.


def home(request):
    t=loader.get_template('home.html')
    pic_indexs=[]
    urls=['http://jandan.net/ooxx/page-%d#comments'% i for i in range(1966,1955,-1)]
    for url in urls:
        res = requests.get(url)
        html = BeautifulSoup(res.text,'lxml')
        for index in html.select('#comments img'):
            pic_indexs.append(index.get('src'))
        time.sleep(0.5)
    c=Context({'pic_indexs':pic_indexs})
    return HttpResponse(t.render(c))