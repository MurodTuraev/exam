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


class MaterialNeededSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    product_materials = serializers.SerializerMethodField()

    class Meta:
        model = CategoryModel
        fields = (
            'name',
            'quantity',
            'product_materials'
        )

    @staticmethod
    def get_product_materials(obj):

        result = []
        quantity = obj.quantity

        for material in obj.product_material.all():
            warehouses = Warehouse.objects.filter(material__id=material.id)

            name = material.material.name
            limit = round((int(quantity) * material.quantity), 4)

            for warehouse in warehouses:

                price = warehouse.price
                if limit > warehouse.remainder:
                    qty = warehouse.remainder
                    limit = limit - qty
                else:
                    qty = limit

                result.append({
                    'warehouse_id': warehouse.id,
                    'material_name': name,
                    'qty': qty,
                    'price': price,
                })

        return result