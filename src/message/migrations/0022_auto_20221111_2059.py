# Generated by Django 3.2 on 2022-11-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0021_auto_20221111_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='refAcces',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='refOrdi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='refPhone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
