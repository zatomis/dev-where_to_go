from django.contrib import admin
# Register your models here.
from places.models import Place, Pictures

admin.site.register(Pictures)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description_short",
    )
