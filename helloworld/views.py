from django.shortcuts import render,redirect,render_to_response   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import musicdata
import random 

def index(request):
	datas = musicdata.objects.all()
	return render(request,'index.html',locals())

def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username =name , password =password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect('home')
		else: 
			message = 'error!'

	return render(request,'login.html',locals())

def register(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']	

		try:
			user = User.objects.get(username = name)
		except:
			user = None

		if user is not None:
			message = 'Username already been used.'
		else:
			user = User.objects.create_user(username = name,password = password)
			user.save()
			message = 'register success.'
			return redirect('home')
	return render(request,'register.html',locals())

def add(request):
	if 'ok' in request.POST:
		artist = request.POST['artist']
		song = request.POST['song']
		url = request.POST['url']
		style = request.POST['style']
		musicdata.objects.create(artist = artist,song = song,url =url, style = style)
		return redirect('home')

	return render_to_response('add.html',locals())

