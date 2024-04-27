from django.contrib import admin
from werehouse import models

# Register your models here.
@admin.register(models.CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    list_display_links = ('name',)


@admin.register(models.RawMaterialModel)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_display_links = ('name',)


@admin.register(models.CategoryRawMaterialModel)
class CategoryRawMaterialAdmin(admin.ModelAdmin):
    list_display = ('category_id','raw_material_id1', 'unit_of_measure1', 'quantity1',
                    'raw_material_id2', 'unit_of_measure2', 'quantity2',
                    'raw_material_id3', 'unit_of_measure3', 'quantity3')
    # search_fields = ('name', )
    list_display_links = ('category_id',)


@admin.register(models.WarehouseModel)
class WarehouseModelAdmin(admin.ModelAdmin):
    list_display = ('id','material_id', 'remainder', 'price')
    # search_fields = ('name', )
    list_display_links = ('material_id',)