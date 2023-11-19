from django.contrib import admin
# Register your models here.
from places.models import Place, Pictures

admin.site.register(Place)
admin.site.register(Pictures)