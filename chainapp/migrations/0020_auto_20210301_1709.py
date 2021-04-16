# Generated by Django 3.1.5 on 2021-03-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chainapp', '0019_auto_20210228_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='images1',
            field=models.ImageField(blank=True, null=True, upload_to='static/products', verbose_name='image1'),
        ),
        migrations.AddField(
            model_name='person',
            name='images2',
            field=models.ImageField(blank=True, null=True, upload_to='static/products', verbose_name='image2'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
