# Generated by Django 4.2.5 on 2023-10-13 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=models.FileField(upload_to='media/proyectos'),
        ),
    ]