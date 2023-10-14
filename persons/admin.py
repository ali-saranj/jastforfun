from django.contrib import admin

# Register your models here.
from .models import Person


@admin.register(Person)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("id","username","name","phone",)
