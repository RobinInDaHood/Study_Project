# Generated by Django 2.2.2 on 2019-06-06 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20190607_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(default='placeholder.png', upload_to='images/pizza'),
        ),
    ]
