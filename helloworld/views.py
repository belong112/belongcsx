from django.shortcuts import render,redirect,render_to_response   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import musicdata
from usersfavorite.models import favlink
import random 

def index(request):
	searchstr = " "
	if request.method == 'POST':
		searchstr = "d"
		searchstr = request.POST['searchstr']	
	datas = musicdata.objects.all()

	return render(request,'index.html',locals())

def addfav(request,song_id,user_id):
	favlink.objects.create(songid = song_id, userid = user_id)
	test = song_id+user_id
	return redirect('home')

def myfav(request,user_id):
	searchstr = " "
	if request.method == 'POST':
		searchstr = request.POST['searchstr']
	m = set()
	link = favlink.objects.all()

	for item in link:
		if item.userid == int(user_id):
			m.add(item.songid)
	datas = musicdata.objects.filter(pk__in = m)

	return render(request,'favorite.html',locals())

def delete(request,song_id,user_id):
	temp = favlink.objects.filter(userid = user_id, songid = song_id)
	temp.delete()
	return redirect('home')

def changepassword(request):
	if request.method == 'POST':
		name = request.POST['name']
		oldpassword = request.POST['oldpassword']	
		newname = request.POST['newpassword']

		user = authenticate(username = name , password = oldpassword)
		
		try:
			userb = User.objects.get(username = newname)
		except:
			userb = None

		if user is not None:
			if user.is_active:
				if userb is not None:
					message = 'Username already been used.'
				# user.set_password(newpassword)
				else:
					user.username = newname
					user.save()
					message = 'username has been changed'
					return redirect('home')
		else:
			message = 'error'

	return render(request,'change.html',locals())

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

