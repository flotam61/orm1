# Generated by Django 4.0.2 on 2022-02-25 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(default='True'),
        ),
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
