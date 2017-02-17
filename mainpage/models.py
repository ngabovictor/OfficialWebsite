from django.db import models

# Create your models here.
class services_all(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	thumbanail_services = models.FileField(upload_to='uploads/services_icons')

	def __str__(self):
		return self.title


class staff(models.Model):
	name = models.CharField(max_length=200)
	posts = models.CharField(max_length=200)
	statement = models.TextField()
	picture = models.FileField(upload_to='uploads/staff_members')

	def __str__(self):
		return self.name


class home_banner(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	banner_image = models.FileField(upload_to='uploads/home_banner')

	def __str__(self):
		return self.title


class services_banner(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	banner_image = models.FileField(upload_to='uploads/services_banner')

	def __str__(self):
		return self.title


class products(models.Model):
	product_thumbnail = models.FileField(upload_to='uploads/products_image', default='null')
	title = models.CharField(max_length=200, default='null')
	caption = models.TextField(default='null')
	App = 'App'
	Web = 'Web'
	Graphics = 'Graphics'
	classification_choices = {
	(App, 'App'),
	(Web, 'Web'),
	(Graphics, 'Graphics'),
	}
	classifications = models.CharField(max_length=200, choices=classification_choices, default="App")
	
	def __str__(self):
		return self.caption

