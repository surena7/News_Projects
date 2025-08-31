from django.contrib import admin
from news import models

class Admin_Post(admin.ModelAdmin):
    list_display=["user","title","status","about","views"]

admin.site.register(models.Post,Admin_Post)
admin.site.register(models.City)
admin.site.register(models.Post_Category)