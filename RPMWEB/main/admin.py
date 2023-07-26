from django.contrib import admin
from .models import Person, Test, Work

admin.site.register(Person)
admin.site.register(Work)
admin.site.register(Test)