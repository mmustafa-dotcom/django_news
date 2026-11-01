
from django.contrib import admin

from .models import News, User, Person, Student


admin.site.register(News)
admin.site.register(User)
admin.site.register(Person)
admin.site.register(Student)
