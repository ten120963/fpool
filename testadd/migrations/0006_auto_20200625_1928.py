# Generated by Django 3.0.7 on 2020-06-25 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testadd', '0005_auto_20200625_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='afce_score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='afcn_score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
