from django.contrib import admin

# Register your models here.
from .models import IPAddress

admin.site.register(IPAddress)