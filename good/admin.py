from django.contrib import admin

from .models import Good, GoodCategory, GoodImage

# admin.site.register(Good)
admin.site.register(GoodCategory)
# admin.site.register(GoodImage)


class ImageInline(admin.TabularInline):
    fk_name = 'good'
    model = GoodImage


@admin.register(Good)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]