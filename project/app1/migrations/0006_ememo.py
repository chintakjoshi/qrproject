# Generated by Django 2.2.1 on 2020-03-18 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20200318_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='ememo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memoDate', models.DateField()),
                ('place', models.CharField(default='', max_length=30)),
                ('rc_data', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app1.rcDetails')),
            ],
        ),
    ]