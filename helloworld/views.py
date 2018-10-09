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
	# data1 = musicdata.objects.create(artist = "the fur", song = "stort stay",url = "https://www.youtube.com/watch?v=X2Ao9sdua4E")
	# data2 = musicdata.objects.create(artist = "per se", song = "wonderline",url ="https://www.youtube.com/watch?v=I2rCFfh50N0")
	# data3 = musicdata.objects.create(artist = "elephant gym", song = "underwater",url = "https://www.youtube.com/watch?v=jDDy-Vh55to")
	datas = musicdata.objects.all()

	random.seed()
	piclist =[]
	for _ in range(15):
		piclist.append(random.randint(1,1500))
	return render(request,'index2.html',locals())

def picture(request,picid):
	return render(request,'picture.html',{'picid':picid})