# Generated by Django 3.2 on 2022-11-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0020_auto_20221111_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='refAcces',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='refOrdi',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='refPhone',
            field=models.CharField(max_length=50),
        ),
    ]
