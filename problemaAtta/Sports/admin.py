from django.contrib import admin

# Register your models here.
from .models import Location, Sports

#admin.site.register(Location)
#admin.site.register(Sports)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'region')

admin.site.register(Location, LocationAdmin)

class SportsAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price', 'startDate', 'endDate')

admin.site.register(Sports, SportsAdmin)