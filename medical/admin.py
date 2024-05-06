from django.contrib import admin
from .models import result

class AdminResult(admin.ModelAdmin):
    list_display = ("id", "temp", "press", "h_rate", "b_oxy", "Sugar")

admin.site.register(result, AdminResult)
