from django.contrib import admin
from .models import Interview, InterviewTimeline, Timeline
# Register your models here.

admin.site.register(InterviewTimeline)
admin.site.register(Timeline)
admin.site.register(Interview)