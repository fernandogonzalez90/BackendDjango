# Generated by Django 5.0.6 on 2024-06-18 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_remove_skills_categoria_remove_softskills_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='softskills',
            name='icon',
        ),
    ]
