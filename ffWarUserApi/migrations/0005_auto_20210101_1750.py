# Generated by Django 3.1.4 on 2021-01-01 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ffWarUserApi', '0004_auto_20210101_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawmodel',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='withdraw', to=settings.AUTH_USER_MODEL),
        ),
    ]
