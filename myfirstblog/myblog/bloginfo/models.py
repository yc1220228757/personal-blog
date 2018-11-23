from django.db import models
from userinfo.models import Userinfo


class Categorya(models.Model):

	name = models.CharField('名称',max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		db_table = "categorya"
		verbose_name = "博客分类"
		verbose_name_plural = verbose_name


class Tag(models.Model):
	tname = models.CharField('名称',max_length=20)

	def __str__(self):
		return self.tname

	class Meta:
		db_table = "tag"
		verbose_name = "标签"
		verbose_name_plural = verbose_name


class Blog(models.Model):
	title = models.CharField('标题',max_length=30,null=False)
	author = models.CharField('作者',max_length=20,null=False)
	content = models.TextField("博文正文")
	created = models.DateTimeField('发布时间',auto_now_add=True)
	picture = models.ImageField('图片',upload_to='static/images/',default='')
	category = models.ForeignKey(Categorya,verbose_name='分类')
	tags = models.ManyToManyField(Tag,verbose_name='标签')
	user = models.ForeignKey(Userinfo,verbose_name='用户')


	def __str__(self):
		return self.title

	class Meta:
		db_table = "blog"
		verbose_name = "博文"
		verbose_name_plural = verbose_name


class Comment(models.Model):
	blog = models.ForeignKey(Blog,verbose_name='博客')
	content = models.CharField('内容',max_length=300)
	created = models.DateTimeField('发布时间',auto_now_add=True)


	def __str__(self):
		return self.content

	class Meta:
		db_table = "comment"
		verbose_name = "评论"
		verbose_name_plural = verbose_name

class Save(models.Model):
	user = models.ForeignKey(Userinfo)
	# blog = models.ForeignKey(Blog)

	def __str__(self):
		return self.blog

	class Meta:
		db_table = "save"
		verbose_name='收藏'
		verbose_name_plural=verbose_name
