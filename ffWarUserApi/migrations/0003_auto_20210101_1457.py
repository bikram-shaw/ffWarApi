# Generated by Django 3.1.4 on 2021-01-01 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ffWarUserApi', '0002_auto_20210101_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to=settings.AUTH_USER_MODEL),
        ),
    ]
