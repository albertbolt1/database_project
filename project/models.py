from django.db import models

# Create your models here.


#class for details of one sportsman
class Sportsman(models.Model):
	name=models.CharField(max_length=20,primary_key=True)
	place_of_birth=models.CharField(max_length=20)
	age=models.IntegerField(null=True)
	height=models.IntegerField(null=True)
	image=models.URLField(max_length=200,null=True,blank=True)


class Competition(models.Model):
	name=models.CharField(max_length=20,primary_key=True)
	description=models.CharField(max_length=50)
	no_of_part=models.IntegerField(null=True)
	image=models.URLField(max_length=200,null=True,blank=True)
	date_year=models.DateField(null=True)
	end_date=models.DateField(null=True)
	place=models.CharField(max_length=20,null=True)


class Event(models.Model):
	id = models.AutoField(primary_key=True)
	Competition_name=models.ForeignKey(Competition,on_delete=models.CASCADE)
	event_name=models.CharField(max_length=20)
	no_of_part=models.IntegerField(null=True)
	



class Records(models.Model):
	id=models.AutoField(primary_key=True)
	player_name=models.ForeignKey(Sportsman,on_delete=models.CASCADE)
	position=models.IntegerField()
	record=models.CharField(max_length=10) 
	event_id=models.ForeignKey(Event,on_delete=models.CASCADE)





