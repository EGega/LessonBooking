from django.contrib import admin

from .models import Teachers, Students, Lessons
# Register your models here.

admin.site.register(Teachers)
admin.site.register(Students)
admin.site.register(Lessons)