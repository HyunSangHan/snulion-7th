# Generated by Django 2.1.7 on 2019-04-17 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='img',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
