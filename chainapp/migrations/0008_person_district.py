# Generated by Django 3.1.5 on 2021-01-10 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chainapp', '0007_auto_20210110_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chainapp.district', verbose_name='Districts'),
        ),
    ]
