# Generated by Django 5.0.9 on 2024-12-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel', '0010_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='intel', verbose_name='Imagen'),
        ),
    ]