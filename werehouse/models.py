from django.db import models
from django.utils import timezone

# Create your models here.

CHOICES_UNIT_OF_MEASUREMENTS = [
    ("dona", "Soni"),
    ("m", "Metr"),
    ("m2", "Metr kvadrat"),
]

class BaseModel(models.Model):
    # Common fields
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class CategoryModel(BaseModel):
    name = models.CharField(max_length=256, verbose_name="Kategoriya nomi")
    code = models.CharField(max_length=256, verbose_name="Kategoriya kodi", unique=True)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name

class RawMaterialModel(BaseModel):
    name = models.CharField(max_length=256, verbose_name="Xomashyo nomi")

    class Meta:
        verbose_name = "Xomashyo"
        verbose_name_plural = "Xomashyolar"

    def __str__(self):
        return self.name


class CategoryRawMaterialModel(BaseModel):
    category_id = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="product")
    raw_material_id1 = models.ForeignKey(RawMaterialModel, on_delete=models.CASCADE, related_name="raw_material_id1", verbose_name="Qaysi xomashyo?")
    unit_of_measure1 = models.CharField(max_length=256, verbose_name="O'lchov birligi", choices=CHOICES_UNIT_OF_MEASUREMENTS)
    quantity1 = models.FloatField(verbose_name="Qancha?")

    raw_material_id2 = models.ForeignKey(RawMaterialModel, on_delete=models.CASCADE, related_name="raw_material_id2", verbose_name="Qaysi xomashyo?")
    unit_of_measure2 = models.CharField(max_length=256, verbose_name="O'lchov birligi",
                                        choices=CHOICES_UNIT_OF_MEASUREMENTS)
    quantity2 = models.FloatField(verbose_name="Qancha?")
    raw_material_id3 = models.ForeignKey(RawMaterialModel, on_delete=models.CASCADE, related_name="raw_material_id3", verbose_name="Qaysi xomashyo?")
    unit_of_measure3 = models.CharField(max_length=256, verbose_name="O'lchov birligi",
                                        choices=CHOICES_UNIT_OF_MEASUREMENTS)
    quantity3 = models.FloatField(verbose_name="Qancha?")

    class Meta:
        verbose_name = "Mahsulot-Material"
        verbose_name_plural = "Mahsulot-Material"

    def __str__(self):
        return str(self.category_id)


class WarehouseModel(BaseModel):
    material_id = models.ForeignKey(RawMaterialModel, on_delete=models.CASCADE, related_name="material", verbose_name="Material ID")
    remainder = models.FloatField(verbose_name="Mahsulot hajmi")
    price = models.FloatField(verbose_name="Bir birlik uchun narx")

    class Meta:
        verbose_name = "Omborxona"
        verbose_name_plural = "Omborxona"

    def __str__(self):
        return str(self.material_id)
