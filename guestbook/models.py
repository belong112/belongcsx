from django.db import models
from django.conf import settings
# Create your models here.


class musicdata(models.Model):
	artist = models.CharField(max_length = 20, blank = True)
	song = models.CharField(max_length = 50, blank = True)
	url = models.CharField(max_length =1000, blank =True)
	vote = models.IntegerField(default = 1000)
	def __str__(self):
		return self.artist + " : " + self.song