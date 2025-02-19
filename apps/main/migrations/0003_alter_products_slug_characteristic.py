# Generated by Django 5.1.5 on 2025-02-03 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_products_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.TextField(null=True, unique=True, verbose_name='SLUG'),
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название характеристики')),
                ('characteristic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.products', verbose_name='Характеристики')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
    ]
