# Generated by Django 2.2.2 on 2019-06-09 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190609_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merch',
            name='image',
            field=models.ImageField(default='/images/shop/placeholder.png', upload_to='images/shop'),
        ),
    ]
