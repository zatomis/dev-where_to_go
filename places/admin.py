from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from places.models import Picture, Place

MAXHEIGHT = 150
MAXWIDTH = 150

@admin.register(Picture)
class PlacePicAdmin(admin.ModelAdmin):
    raw_id_fields = ['place_pic']


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Picture
    extra = 1
    readonly_fields = ["get_pic_preview"]

    def get_pic_preview(self, model):
        return format_html('<img src="{}" style="max-height:{}px; max-width:{}px;"/>', mark_safe(model.picture.url), MAXHEIGHT, MAXWIDTH)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    readonly_fields = ["place_order", "slug"]

    list_display = (
        "id",
        "title",
        "short_description",
    )
    inlines = (ImageInline, )
