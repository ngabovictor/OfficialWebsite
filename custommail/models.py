from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class mailbox(models.Model):
	name = models.CharField(max_length=300)
	email = models.EmailField()
	message = models.TextField()
	date = models.DateField(default=datetime.today())
	Read = 'Read'
	Unread = 'Unread'
	classification_choices = {
	(Read, 'Read'),
	(Unread, 'Unread'),
	}
	classifications = models.CharField(max_length=200, choices=classification_choices, default="Unread")

	def __str__(self):
	    return self.name

	def __iter__(self):
		return self.classifications
