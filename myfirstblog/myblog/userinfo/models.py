from django.db import models

class Userinfo(models.Model):
	uname = models.CharField(max_length=20,null=False)
	upassword = models.CharField(max_length=200,null=False)
	email = models.EmailField(null=True)
	phone = models.IntegerField(null=False)
	time = models.DateTimeField('注册时间',auto_now=True)
	
	def __str__(self):
		return self.uname

	class Meta:
		db_table = "userinfo"
		verbose_name = '登录用户'
		verbose_name_plural=verbose_name


