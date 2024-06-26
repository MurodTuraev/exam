# Generated by Django 5.0.4 on 2024-04-27 18:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werehouse', '0003_alter_categoryrawmaterialmodel_raw_material_id1_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryrawmaterialmodel',
            options={'verbose_name': 'Mahsulot-Material', 'verbose_name_plural': 'Mahsulot-Material'},
        ),
        migrations.CreateModel(
            name='WarehouseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remainder', models.FloatField(verbose_name='Mahsulot hajmi')),
                ('price', models.FloatField(verbose_name='Bir birlik uchun narx')),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material', to='werehouse.rawmaterialmodel', verbose_name='Material ID')),
            ],
            options={
                'verbose_name': 'Omborxona',
                'verbose_name_plural': 'Omborxona',
            },
        ),
    ]
