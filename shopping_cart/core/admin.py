from django.contrib import admin
from django.utils.html import format_html

from core.models import Item,ItemTag,ItemImage,Category

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    prepopulated_fields = {'slug':('name', )}
@admin.register(ItemTag)
class ItemTagAdmin(admin.ModelAdmin):
    list_display = ['name','active']

    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(ItemImage)
class ItemImage(admin.ModelAdmin):
    list_display = ['thumbnail_tag','item']
    readonly_fields = ('thumbnail',)

    def thumbnail_tag(self, obj):
        if obj.thumbnail:
            return format_html('<img src="%s" height="50px" width="50px"/>'% obj.thumbnail.url)
        return "-"
    thumbnail_tag.short_description="Thumbnail"
    def item_name(self,obj):
        return obj.name


