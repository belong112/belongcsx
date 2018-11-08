from django.db import models
from django.conf import settings
# Create your models here.

class favlink(models.Model):
	userid = models.IntegerField(blank = False)
	songid = models.IntegerField(blank = False)
	def __str__(self):
		return str(self.userid) + " with " + str(self.songid)
# Create your models here.
