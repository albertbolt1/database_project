from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'project'
urlpatterns=[
	path('home/', views.home, name='start'),
	path('teja/',views.teja,name='teja'),
	path('',views.first,name='first'),
	path('second/',views.second,name='second'),
	path('third/',views.third,name='third'),
	path('fourth/',views.fourth,name='fourth'),
	path('fifth/',views.fifth,name='fifth'),
	path('sixth/',views.sixth,name='sixth'),
	path('seventh/',views.seventh,name='seven'),
	path('eigth/',views.eigth,name='eigth'),
	path('nine/',views.nine,name='nine'),
	path('eleven/',views.eleven,name='eleven'),
	path('twelve/',views.twelve,name='twelve'),
	path('twenty/',views.twenty,name='twenty'),
	path('thirteen/',views.thirteen,name='thirteen'),
	path('knowabout/',views.knowaboutolympicyear,name='knowaboutolympicyear1'),
	path('aboutolympicyear/',views.aboutolympicyear,name='aboutolympicyear'),
	path('videosyou/',views.youtube,name='videosyou'),
	#path('developer1/',views.aboutdeveloper1,name='dev1'),
	#path('developer2/',views.aboutdeveloper2,name='dev2'),
]