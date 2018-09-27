from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random 

# for i in xrange(1,15):
# 	piclist.append(random.randint(0,1000))

def index(request):
	random.seed(99)
	piclist =[]
	for _ in range(15):
		piclist.append("https://picsum.photos/200/200/?image="+str(random.randint(1,1000)))
	return render(request,'index2.html',{'piclist':piclist})