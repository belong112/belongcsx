from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import musicdata
import random 

# for i in xrange(1,15):
# 	piclist.append(random.randint(0,1000))

def index(request):
	# data1 = musicdata.objects.create(artist = "The fur", song = "stort stay",url = "X2Ao9sdua4E",style = "Alter")
	# data2 = musicdata.objects.create(artist = "Per se", song = "wonderline",url ="I2rCFfh50N0",style = "Folk")
	# data3 = musicdata.objects.create(artist = "Elephant gym", song = "underwater",url = "jDDy-Vh55to",style = "Rock")
	datas = musicdata.objects.all()
	# random.seed()
	# piclist =[]
	# for _ in range(15):
	# 	piclist.append(random.randint(1,1500))
	return render(request,'index.html',locals())

def picture(request,picid):
	return render(request,'picture.html',{'picid':picid})

def add(request):
	if 'ok' in request.POST:
		artist = request.POST['artist']
		song = request.POST['song']
		url = request.POST['url']
		style = request.POST['style']
		musicdata.objects.create(artist = artist,song = song,url =url, style = style)
	return render(request,'add.html',locals())

def newdata(request):
	if 'ok' in request.POST:
		artist = request.POST['artist']
		song = request.POST['song']
		url = request.POST['url']
		style = request.POST['style']
		musicdata.objects.create(artist = artist,song = song,url =url, style = style)
	return render(request,'add.html',locals())
