# Generated by Django 5.0.6 on 2024-07-22 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_alter_certificaciones_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='view_live',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]