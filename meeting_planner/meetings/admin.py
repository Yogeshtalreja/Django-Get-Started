from django.contrib import admin

# Register your models here.
from .models import Model
admin.site.register(Model)
from .models import Room
admin.site.register(Room)