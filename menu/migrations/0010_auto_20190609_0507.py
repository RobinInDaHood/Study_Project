# Generated by Django 2.2.2 on 2019-06-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20190609_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='image',
            field=models.ImageField(default='/images/drinks/placeholder_soda.png', upload_to='images/drinks'),
        ),
    ]
