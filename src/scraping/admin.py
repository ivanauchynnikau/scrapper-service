from django.contrib import admin
from .models import City, Language, Vacancy, Error, Url

# Register your models here.

admin.site.register(City)
admin.site.register(Language)
admin.site.register(Vacancy)
admin.site.register(Error)
admin.site.register(Url)
