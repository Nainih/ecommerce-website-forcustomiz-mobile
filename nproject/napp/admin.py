from django.contrib import admin
from napp.models import  mobileCustamisation,buy

from django.contrib.sessions.models import Session
# Register your models here.
admin.site.register(Session)

#admin.site.register(mobileCustamisation)
@admin.register(mobileCustamisation)
class mobileCustamisationAdmin(admin.ModelAdmin):
    list_display=['id','brand','size_of_screen','proceseor','ram','camera','customorID']


admin.site.register(buy)