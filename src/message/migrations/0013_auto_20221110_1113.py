# Generated by Django 3.2 on 2022-11-10 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0012_auto_20221110_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='acces',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='message.acces'),
        ),
        migrations.AlterField(
            model_name='message',
            name='ordinateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='message.ordinateur'),
        ),
        migrations.AlterField(
            model_name='message',
            name='telephone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='message.telephone'),
        ),
    ]
