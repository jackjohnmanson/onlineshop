# Generated by Django 2.2.6 on 2019-11-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_product_publish_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='publish_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
