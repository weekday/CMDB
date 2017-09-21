#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login.html')
def index(request):  #首页
	return render(request,'index.html',locals())

def login_view(request):
	if request.method == 'POST' and request.POST:
		u = request.POST['username']
		p = request.POST['password']
		user = authenticate(username = u,password =p)
		if user is not None:
			if user.is_active:
				login(request,user)
				request.session['user'] = u
				request.session['is_login'] = True
				return redirect('/index.html')
			else:
				error_msg1 = '用户名或密码错误，请重试'
				return render(request,'login.html',{'error_msg':error_msg1})
		else:
			error_msg1 = '用户名或密码错误，请重试'
			return render(request, 'login.html', {'error_msg': error_msg1})
	else:
		error_msg = '请登录'
		return render(request,'login.html',{'error_msg':error_msg})

def logout(request):
	try:
		del request.session['user']
		del request.session['is_login']
	except KeyError:
		pass
	return HttpResponse("You're logged out.")

@login_required(login_url='/login.html')
def error(request):
	return render(request,'error.html')


