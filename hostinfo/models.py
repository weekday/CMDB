#coding:utf-8
from django.db import models

# Create your models here.
class Host(models.Model):
	hostname = models.CharField(max_length=64,verbose_name='主机编号')
	ip = models.GenericIPAddressField(verbose_name='IP地址',null=True)
	port = models.CharField(max_length=10,verbose_name='端口',null=True)
	username = models.CharField(max_length=64,verbose_name='登录用户',null=True)
	password = models.CharField(max_length=64,verbose_name='登录密码',null=True)
	jifang = models

	osversion = models.CharField(max_length=64,verbose_name='系统版本',null=True)
	memory = models.CharField(max_length=64,verbose_name='内存',null=True)
	disk = models.CharField(max_length=64,verbose_name='硬盘',null=True)
	sn = models.CharField(max_length=64,verbose_name='SN号',null=True)
	model_name = models.CharField(max_length=64,verbose_name='型号',null=True)
	cpu = models.CharField(max_length=64,verbose_name='CPU',null=True)
	remarks = models.CharField(max_length=1000,verbose_name='备注',null=True)

	class Meta:
		db_table = 'Host'
		verbose_name = '主机信息'
		verbose_name_plural = '主机信息'

	def __str__(self):
		return self.hostname


class History(models.Model):
	ip = models.GenericIPAddressField(verbose_name='IP',null=True)
	root = models.CharField(max_length=64,verbose_name='用户',null=True)
	port = models.CharField(max_length=10,verbose_name='端口',null=True)
	cmd = models.CharField(max_length=64,verbose_name='命令',null=True)
	user = models.CharField(max_length=64,verbose_name='操作者',null=True)
	ctime = models.DateTimeField(auto_now_add=True,null=True,verbose_name='操作时间')

	class Meta:
		db_table = 'History'
		verbose_name = '历史操作'
		verbose_name_plural = '历史操作'

	def __str__(self):
		return self.user


class Business(models.Model):
	caption = models.CharField(max_length=64,verbose_name='机房',null=True)
	address = models.CharField(max_length=100,verbose_name='机房地址',null=True)
	contacts = models.CharField(max_length=64,verbose_name='联系人',null=True)
	conphone = models.CharField(max_length=16,verbose_name='联系电话',null=True)
	ctime = models.DateTimeField(auto_now_add=True,verbose_name='录入时间',null=True)
	remarks = models.CharField(max_length=1000,verbose_name='备注',null=True)

	class Meta:
		db_table = 'Business'
		verbose_name = '机房信息'
		verbose_name_plural = '机房信息'

	def __str__(self):
		return self.caption
