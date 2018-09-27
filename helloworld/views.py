from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random 

# for i in xrange(1,15):
# 	piclist.append(random.randint(0,1000))

def index(request):
	# random.seed(99)
	# piclist = [random.randint(1,1000) for _ in range(15)]
	piclist = [1,2,3,4,5]
	return render(request,'index2.html',{'piclist':piclist})