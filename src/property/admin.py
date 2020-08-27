from django.contrib import admin

# Register your models here.
from .models import Property, Category, Reserve

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name' ,'category' ,'property_type' , 'area' , 'beds_number' , 'baths_number' , 'garages_number']
    search_fields = ['name' , 'property_type']
    search_fields = ['name' , 'property_type']
    list_filter=['category','property_type']
admin.site.register(Property, PropertyAdmin)
admin.site.register(Category)
admin.site.register(Reserve)