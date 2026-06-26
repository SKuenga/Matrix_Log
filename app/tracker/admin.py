from django.contrib import admin
# Register your models here.
from .models import Student, SessionLog
admin.site.register([Student, SessionLog])
