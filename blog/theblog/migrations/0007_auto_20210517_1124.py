# Generated by Django 3.1.7 on 2021-05-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_auto_20210517_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Coding stuff', max_length=255),
        ),
    ]
