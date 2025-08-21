from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Superhero)
# class SuperheroAdmin(admin.ModelAdmin):
#     list_display = ('name', 'power')   # show these fields in the admin list
#     search_fields = ('name', 'power')  # add search box