from django.contrib import admin

from .models import Event,Competition,Sportsman,Records
# Register your models here.


admin.site.register(Event)
admin.site.register(Competition)
admin.site.register(Sportsman)
admin.site.register(Records)


