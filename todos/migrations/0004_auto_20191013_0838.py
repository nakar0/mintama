# Generated by Django 2.2.4 on 2019-10-12 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20191009_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='order',
            field=models.IntegerField(default=9999),
        ),
    ]
