from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from places.models import Place, Picture
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase

class PlacePicAdmin(admin.ModelAdmin):
    raw_id_fields = ['place_pic']


admin.site.register(Picture, PlacePicAdmin)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Picture
    extra = 1
    readonly_fields = ["_pic_preview"]

    def _pic_preview(self, model):
        return format_html('<img src="{}" style="max-height:150px; width:auto"/>', mark_safe(model.picture.url))


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    readonly_fields = ["place_order", "unique_location"]

    list_display = (
        "id",
        "title",
        "short_description",
    )
    inlines = (ImageInline, )
