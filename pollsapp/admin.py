from django.contrib import admin
from pollsapp.models import Question, Choice ,newpolls

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(newpolls)

