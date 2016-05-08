from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
import requests
from bs4 import BeautifulSoup
import time
from pic_blog.models import Picture

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Django'})

def picture(request):
    pic_indexs=[]
    pics=[]
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
    'Referer':'http://jandan.net/ooxx/page-1980'}
    urls=['http://jandan.net/ooxx/page-%d#comments'% i for i in range(1979,1975,-1)]
    for url in urls:
        res = requests.get(url,headers=headers)
        html = BeautifulSoup(res.text,'lxml')
        for index in html.select('#comments img'):
            pic_indexs.append(index.get('src'))
        time.sleep(0.5)
    for pic in pic_indexs:
        name=pic[:10]
        index=pic
        pictures=Picture(name=name,index=index)
        pics.append(pictures)
    Picture.objects.bulk_create(pics)
    picture=Picture.objects.all()
    return render(request,'picture.html',{'pics':picture})