from django.db import models

class Information(models.Model):
	Gender = ((u'M', u'Male'), (u'F', u'Female'))
	name = models.CharField(max_length = 20)
	sex = models.CharField(max_length = 2, choices = Gender,verbose_name='Gender')
	number = models.CharField(blank = True, max_length = 8)
	popo = models.EmailField(blank = True)
	phone = models.CharField(blank = True, max_length = 15)
	'''
	def __unicode__(self):
		return self.name
	'''
	class Meta:
		ordering = ['name']
