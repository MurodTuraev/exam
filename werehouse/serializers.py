from rest_framework import serializers
from werehouse.models import CategoryModel, RawMaterialModel, CategoryRawMaterialModel, WarehouseModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('name','code')


class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterialModel
        fields = ('name',)


class CategoryRawMaterialSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer(read_only=True)
    raw_material_id1 = RawMaterialSerializer(read_only=True)
    raw_material_id2 = RawMaterialSerializer(read_only=True)
    raw_material_id3 = RawMaterialSerializer(read_only=True)
    class Meta:
        model = CategoryRawMaterialModel
        fields = ('category_id', 'raw_material_id1', 'unit_of_measure1', 'quantity1',
                  'raw_material_id2', 'unit_of_measure2', 'quantity2',
                  'raw_material_id3', 'unit_of_measure3', 'quantity3')


class WarehouseSerializer(serializers.ModelSerializer):
    material_id = RawMaterialSerializer(read_only=True)
    class Meta:
        model = WarehouseModel
        fields = ('material_id','remainder','price')