from django.contrib import admin
from.models import *
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('name',)} #чтобы слаг формировался автоматически


admin.site.register(Room, RoomAdmin)
admin.site.register(Message)
