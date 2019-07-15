from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()

	def __str__(self):
		return self.title

class Store(models.Model):
	GPSX = models.CharField(max_length=50)
	GPSY = models.CharField(max_length=50)
	LARG_CATE = models.CharField(max_length=50)
	MID_CATE = models.CharField(max_length=50)
	SMALL_CATE = models.CharField(max_length=50)
	NAME = models.CharField(max_length=50)
	IMAGENAME = models.CharField(max_length=50)
	IMAGE = models.ImageField(default='media/default_image.jpg')	
	def __str__(self):
		return self.NAME

class Place(models.Model):
	GPSX = models.CharField(max_length=50)
	GPSY = models.CharField(max_length=50)
	LARG_CATE = models.CharField(max_length=50)
	MID_CATE = models.CharField(max_length=50)
	SMALL_CATE = models.CharField(max_length=50)
	NAME = models.CharField(max_length=50)
	IMAGENAME = models.CharField(max_length=50)
	IMAGE = models.ImageField(default='media/default_image.jpg')

	def __str__(self):
		return self.NAME
