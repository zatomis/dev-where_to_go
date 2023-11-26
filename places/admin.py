from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from places.models import Place, Pictures

admin.site.register(Pictures)


class ImageInline(admin.TabularInline):
    model = Pictures
    extra = 1
    readonly_fields = ["pic_preview"]

    def pic_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 150px;"/>', mark_safe(obj.picture.url))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description_short",
    )
    inlines = (ImageInline, )
