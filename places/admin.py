from django.contrib import admin
from places.models import Place, Pictures

admin.site.register(Pictures)


class ImageInline(admin.TabularInline):
    model = Pictures
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description_short",
    )
    inlines = (ImageInline, )
