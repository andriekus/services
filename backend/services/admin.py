from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'availability')

admin.site.register(Service, ServiceAdmin)
