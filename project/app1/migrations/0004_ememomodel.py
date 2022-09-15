# Generated by Django 2.2.1 on 2020-03-17 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200220_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='ememoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicletype', models.CharField(default='', max_length=20)),
                ('ememodate', models.DateField()),
                ('vehicleno', models.CharField(default='', max_length=25)),
                ('ememono', models.CharField(default='', max_length=25)),
                ('place', models.CharField(default='', max_length=50)),
                ('vehiclemake', models.CharField(default='', max_length=25)),
                ('vehiclemodel', models.CharField(default='', max_length=25)),
                ('fine', models.PositiveIntegerField(default='')),
                ('user_data', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app1.LoginForm')),
            ],
        ),
    ]
