from django.db import models
class Newuser(models.Model):
	p_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	age=models.CharField(max_length=100)
	gender=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	confirm=models.CharField(max_length=100)
	address=models.TextField(max_length=500)
	def __str__(self):
		return self.name
class Blood(models.Model):
	p_id = models.AutoField(primary_key=True)
	btype=models.CharField(max_length=100)
	state=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	bankname=models.CharField(max_length=100)
	nounit=models.CharField(max_length=100)
	price=models.TextField(max_length=500)
	def __str__(self):
		return self.btype
class Camp(models.Model):
	p_id = models.AutoField(primary_key=True)
	cname=models.CharField(max_length=100)
	state=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	noday=models.CharField(max_length=100)
	def __str__(self):
		return self.cname
class Bloodrequest(models.Model):
	p_id = models.AutoField(primary_key=True)
	bname=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	state=models.CharField(max_length=100)
	bloodid=models.CharField(max_length=100)
	nounit=models.CharField(max_length=100)
	price=models.CharField(max_length=100)
	total=models.CharField(max_length=100)
	def __str__(self):
		return self.bname

class Bloodbank(models.Model):
	p_id = models.AutoField(primary_key=True)
	no=models.CharField(max_length=100)
	h_name=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	blood_type=models.CharField(max_length=100)
	av_or_not=models.CharField(max_length=100)
	def __str__(self):
		return self.no

# Create your models here.
