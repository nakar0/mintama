# Generated by Django 2.2.4 on 2019-11-10 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191031_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='temp_data',
            field=models.CharField(blank=True, max_length=20000),
        ),
        migrations.AlterField(
            model_name='reference',
            name='content',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='reference',
            name='link',
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='reference',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
