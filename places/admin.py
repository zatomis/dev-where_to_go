from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from places.models import Place, Picture
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase


admin.site.register(Picture)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Picture
    extra = 1
    readonly_fields = ["_pic_preview"]

    def _pic_preview(self, obj):
        return format_html('<img src="{}" style="max-height:150px; width:auto"/>', mark_safe(obj.picture.url))


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    readonly_fields = ["place_order", "placeID"]

    list_display = (
        "id",
        "title",
        "description_short",
    )
    inlines = (ImageInline, )
