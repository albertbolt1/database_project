# Generated by Django 2.0 on 2020-03-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20200308_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='record',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
