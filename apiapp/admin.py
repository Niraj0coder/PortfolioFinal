from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(technologies)
admin.site.register(education)
admin.site.register(experiences)
admin.site.register(projects)