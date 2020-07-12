from django.shortcuts import render
import json
from django.forms.models import model_to_dict
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import Event,Competition,Sportsman,Records
from django import template

from .forms import sportsman,recordsportsman,competition,forgraph,yearwiseresult,graphcountry
from .choices import some
import tkinter
from django.http import HttpResponse

from django.template import loader

import datetime
import matplotlib as mpl, matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import django
import django
choices=some()

choice1=choices[0]
choice2=choices[1]
choice3=choices[2]

def home(request):

	a=Records.objects.all().filter(player_name__place_of_birth="Jamaica")

	return render(request, 'project/home.html',{'a':a})


def first(request):

	return render(request, 'project/first.html')

def second(request):

	return render(request, 'project/second.html')

def third(request):
	if request.method == 'POST': 
		form = sportsman(request.POST)
		form.fields['name'].choices = [(i,i) for i in choice1]
		if form.is_valid(): 
			b=form.cleaned_data['name']
			b=str(b)
			a=Records.objects.all().filter(player_name__name=b)
			return render(request, 'project/third.html',{'a':a,'b':b})



def fourth(request):
	if request.method == 'POST': 
		form = sportsman(request.POST)
		form.fields['name'].choices = [(i,i) for i in choice1]
		if form.is_valid(): 
			b=form.cleaned_data['name']
			b=str(b)
			a=Records.objects.all().filter(player_name__name=b)
			return render(request, 'project/third.html',{'a':a})


	return render(request, 'project/fourth.html')



def fifth(request):
	if request.method == 'POST': 
		form = competition(request.POST)
		form.fields['name'].choices = [(i,i) for i in choice2]
		form.fields['event'].choices = [(i,i) for i in choice3]
		if form.is_valid(): 
			b=form.cleaned_data['name']
			c=form.cleaned_data['event']
			a=Records.objects.all().filter(event_id__event_name=c,event_id__Competition_name__name=b)
			return render(request, 'project/fifth.html',{'a':a,'b':b,'c':c})


def sixth(request):
	form = graphcountry()
	form.fields['competition'].choices = [(i,i) for i in choice2]


	return render(request, 'project/sixth.html',{'form':form})



def seventh(request):
	form = sportsman()
	form.fields['name'].choices = [(i,i) for i in choice1]
	return render(request, 'project/seventh.html',{'form':form})

def eigth(request):
	form = recordsportsman() 
	form.fields['name'].choices = [(i,i) for i in choice1]

	return render(request, 'project/eigth.html',{'form':form})


def nine(request):
	form = competition() 
	form.fields['name'].choices = [(i,i) for i in choice2]
	form.fields['event'].choices = [(i,i) for i in choice3]


	return render(request, 'project/nine.html',{'form':form})


def eleven(request):
	form = forgraph() 
	form.fields['name'].choices = [(i,i) for i in choice1]
	form.fields['event'].choices = [(i,i) for i in choice3]


	return render(request, 'project/eleven.html',{'form':form})


def twelve(request):
	if request.method == 'POST': 
		form = forgraph(request.POST)
		form.fields['name'].choices = [(i,i) for i in choice1]
		form.fields['event'].choices = [(i,i) for i in choice3]
		if form.is_valid(): 
			b=form.cleaned_data['name']
			c=form.cleaned_data['event']

			import mysql.connector
			mydb = mysql.connector.connect(
				host="localhost",
				user="root",
				passwd="albertbolt23",
  				database="sports2",
  				auth_plugin='mysql_native_password'
  				)

			mycursor = mydb.cursor()

			sql = "SELECT record,date_year FROM project_records,project_event,project_competition where project_records.event_id_id=project_event.id and project_event.Competition_name_id=project_competition.name and project_records.player_name_id='%s' and project_event.event_name='%s' order by date_year"%(b,c)

			mycursor.execute(sql)

			k = mycursor.fetchall()

			a=[]
			for i in k:
				for j in i:
					a.append(j)
			print(a)
			a23=[]
			a24=[]
			if(len(a)!=0):
				k=a[0][len(a[0])-1]
			for i in range(0,len(a),2):
				a23.append(a[i][:len(a[i])-1])
			print(a23)
			for i in range(1,len(a),2):
				a24.append(a[i])

			if(len(a23)==0):
				return render(request,"project/warningnogamesplayed.html");


			a25=[]
			if(k=='s'):
				for i in a23:
					b=i.split(":")
					b=[float(i) for i in b]
					if(len(b)==3):
						d=b[0]*3600*1000+b[1]*60*1000+b[2]*1000
						a25.append(d)

					elif(len(b)==2):
						d=b[0]*60*1000+b[1]*1000
						a25.append(d)
					else:
						d=b[0]*1000
						a25.append(d)

				fig = Figure(figsize=(10,5))
				canvas = FigureCanvas(fig)
				ax = fig.add_subplot(111)
				ax.scatter(a24,a25)
				ax.plot(a24, a25)
				ax.set_xlabel('Date of record')
				ax.set_ylabel('Record timing(in ms)')
				plt.gcf().autofmt_xdate()
				response = HttpResponse(content_type='image/jpg')
				canvas.print_jpg(response)

				return response


def thirteen(request):
	if request.method == 'POST': 
		form = graphcountry(request.POST)
		form.fields['competition'].choices = [(i,i) for i in choice2]
		if form.is_valid(): 
			b=form.cleaned_data['competition']

			import mysql.connector
			mydb = mysql.connector.connect(
				host="localhost",
				user="root",
				passwd="albertbolt23",
  				database="sports2",
  				auth_plugin='mysql_native_password'
  				)

			mycursor = mydb.cursor()

			sql = "SELECT place_of_birth,count(*) FROM project_records,project_event,project_competition,project_sportsman where project_records.event_id_id=project_event.id and project_event.Competition_name_id=project_competition.name and project_records.player_name_id=project_sportsman.name and project_competition.name='%s' group by place_of_birth order by count(*)"%(b)

			mycursor.execute(sql)

			k = mycursor.fetchall()

			a=[]
			for i in k:
				for j in i:
					a.append(j)
			a23=[]
			a24=[]
			

			for i in range(0,len(a),2):
				a23.append(a[i])
			for i in range(1,len(a),2):
				a24.append(a[i])

			y_pos = np.arange(len(a23))

			fig = Figure(figsize=(10,5))
			canvas = FigureCanvas(fig)
			ax = fig.add_subplot(111)
			y_pos = np.arange(len(a23))
			ax.barh(a23,a24, align='center', alpha=0.5)
			ax.set_xlabel('No of medals')
			ax.set_ylabel('Countries')

			response = HttpResponse(content_type='image/jpg')
			canvas.print_jpg(response)

			return response

def teja(request):

	a=Records.objects.all().filter(player_name="Usain Bolt")
	b=[]
	c=[]
	for i in a:
		k=i.__dict__
		k1=i.event_id.date
		k2=k1.year
		b.append(k2)
		c.append(i.record)

	a=[b,c]
	"""a=a[0].__dict__
	a=a['record']"""

	"""a = serializers.serialize('json',a)"""
	return render(request, 'project/teja.html',{'a':a})




def twenty(request):
	if request.method == 'POST': 
		form = sportsman(request.POST)
		form.fields['name'].choices = [(i,i) for i in choice1]
		if form.is_valid(): 
			b=form.cleaned_data['name']
			b=str(b)
			a=Sportsman.objects.all().filter(name=b)
			return render(request, 'project/twenty.html',{'a':a})



def knowaboutolympicyear(request):
	form = graphcountry()
	form.fields['competition'].choices = [(i,i) for i in choice2]


	return render(request, 'project/knowaboutolympicyear.html',{'form':form})


def aboutolympicyear(request):
	if request.method == 'POST': 
		form = graphcountry(request.POST)
		form.fields['competition'].choices = [(i,i) for i in choice2]
		if form.is_valid(): 
			b=form.cleaned_data['competition']
			b=str(b)
			a=Competition.objects.all().filter(name=b)
			return render(request, 'project/aboutolympicyear.html',{'a':a})



def youtube(request):
	return render(request,'project/videos.html')


"""def aboutdeveloper1(request):
	return render(request,'project/aboutdeveloper1.html')

def aboutdeveloper2(request):
	return render(request,'project/aboutdeveloper1.html')

"""