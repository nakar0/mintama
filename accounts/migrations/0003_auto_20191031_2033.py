# Generated by Django 2.2.4 on 2019-10-31 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_default_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='default_board',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='default_user', to='todos.Board'),
        ),
    ]
