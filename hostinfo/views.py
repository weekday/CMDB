#coding:utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
from models import Host,History,Business
# Create your views here.
@login_required(login_url='/login.html')
def host(request):
	host = Host.objects.filter(id__gt = 0)
	jifang_list = Business.objects.all()
	return render(request,'host/host.html',{'host_list':host,'jifang_list':jifang_list})

@login_required(login_url='/login.html')
@permission_required('hostinfo.add_host',login_url='/error.html')
def host_add(request):  #添加主机
	ret = {'status':True,'error':None,'data':None}
	if request.method == 'POST':
		try:
			ip = request.POST.get('ip',None)
			port =
