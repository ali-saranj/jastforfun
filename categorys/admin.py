from django.contrib import admin

from .models import Category


# Register your models here.

@admin.register(Category)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("name",)
