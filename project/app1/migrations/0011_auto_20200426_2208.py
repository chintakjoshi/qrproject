# Generated by Django 3.0.5 on 2020-04-26 22:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20200426_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifydocument',
            name='unique',
            field=models.UUIDField(blank=True, default=uuid.uuid4),
        ),
    ]
