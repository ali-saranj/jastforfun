from django.contrib import admin

from .models import Salon


# Register your models here.

@admin.register(Salon)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("name",)
