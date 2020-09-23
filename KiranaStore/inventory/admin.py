from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(VegetableFruit, GroceryStaple, HouseholdItem, PersonalCare, SnacksBeverage)
class ViewAdmin(ImportExportModelAdmin):
    pass