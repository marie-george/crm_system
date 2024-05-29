from django.contrib import admin

from .models import Good, GoodCategory, GoodImage, GoodColor, GoodReview, Deal, Favourite

admin.site.register(GoodCategory)


class ImageInline(admin.TabularInline):
    fk_name = 'good'
    model = GoodImage


@admin.register(Good)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]


admin.site.register(GoodColor)
admin.site.register(GoodReview)
admin.site.register(Deal)
admin.site.register(Favourite)