from django.contrib import admin

# Register your models here.
from catalog.models import Product, Category, Version

# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'purchase_price', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'version_name', 'version_number')


