# Generated by Django 5.0.9 on 2024-12-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel', '0009_documentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='App', verbose_name='Imagen'),
        ),
    ]
