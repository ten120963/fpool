# Generated by Django 3.0.7 on 2020-06-24 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testadd', '0003_auto_20200624_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='afce_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='afcn_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teams',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
