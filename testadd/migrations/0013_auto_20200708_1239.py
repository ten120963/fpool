# Generated by Django 3.0.7 on 2020-07-08 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testadd', '0012_auto_20200707_1354'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='games',
            name='unique_away',
        ),
        migrations.RemoveConstraint(
            model_name='games',
            name='unique_home',
        ),
    ]
