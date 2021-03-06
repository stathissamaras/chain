# Generated by Django 3.1.5 on 2021-03-29 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chainapp', '0034_auto_20210329_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='job',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='mobile',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='vat',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.RemoveField(
            model_name='alternative',
            name='product',
        ),
        migrations.AddField(
            model_name='alternative',
            name='product',
            field=models.ManyToManyField(to='chainapp.Product'),
        ),
    ]
