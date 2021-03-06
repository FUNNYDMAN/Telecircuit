# Generated by Django 2.0 on 2018-06-09 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=250)),
                ('power', models.CharField(blank=True, max_length=250)),
                ('main', models.CharField(blank=True, max_length=250)),
                ('t_con', models.CharField(blank=True, max_length=250)),
                ('x_main', models.CharField(blank=True, max_length=250)),
                ('y_main', models.CharField(blank=True, max_length=250)),
                ('logic', models.CharField(blank=True, max_length=250)),
                ('inverter', models.CharField(blank=True, max_length=250)),
                ('y_skan', models.CharField(blank=True, max_length=250)),
                ('other', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Dell',
            },
        ),
        migrations.CreateModel(
            name='Horizont',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=250)),
                ('power', models.CharField(blank=True, max_length=250)),
                ('main', models.CharField(blank=True, max_length=250)),
                ('t_con', models.CharField(blank=True, max_length=250)),
                ('x_main', models.CharField(blank=True, max_length=250)),
                ('y_main', models.CharField(blank=True, max_length=250)),
                ('logic', models.CharField(blank=True, max_length=250)),
                ('inverter', models.CharField(blank=True, max_length=250)),
                ('y_skan', models.CharField(blank=True, max_length=250)),
                ('other', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Horizont',
            },
        ),
        migrations.CreateModel(
            name='LG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=250)),
                ('power', models.CharField(blank=True, max_length=250)),
                ('main', models.CharField(blank=True, max_length=250)),
                ('t_con', models.CharField(blank=True, max_length=250)),
                ('x_main', models.CharField(blank=True, max_length=250)),
                ('y_main', models.CharField(blank=True, max_length=250)),
                ('logic', models.CharField(blank=True, max_length=250)),
                ('inverter', models.CharField(blank=True, max_length=250)),
                ('y_skan', models.CharField(blank=True, max_length=250)),
                ('other', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'LG',
            },
        ),
        migrations.CreateModel(
            name='Panasonic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=250)),
                ('power', models.CharField(blank=True, max_length=250)),
                ('main', models.CharField(blank=True, max_length=250)),
                ('t_con', models.CharField(blank=True, max_length=250)),
                ('x_main', models.CharField(blank=True, max_length=250)),
                ('y_main', models.CharField(blank=True, max_length=250)),
                ('logic', models.CharField(blank=True, max_length=250)),
                ('inverter', models.CharField(blank=True, max_length=250)),
                ('y_skan', models.CharField(blank=True, max_length=250)),
                ('other', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Panasonic',
            },
        ),
        migrations.CreateModel(
            name='Philips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=250)),
                ('power', models.CharField(blank=True, max_length=250)),
                ('main', models.CharField(blank=True, max_length=250)),
                ('t_con', models.CharField(blank=True, max_length=250)),
                ('x_main', models.CharField(blank=True, max_length=250)),
                ('y_main', models.CharField(blank=True, max_length=250)),
                ('logic', models.CharField(blank=True, max_length=250)),
                ('inverter', models.CharField(blank=True, max_length=250)),
                ('y_skan', models.CharField(blank=True, max_length=250)),
                ('other', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Philips',
            },
        ),
        migrations.CreateModel(
            name='Samsung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=250)),
                ('power', models.CharField(blank=True, max_length=250)),
                ('main', models.CharField(blank=True, max_length=250)),
                ('t_con', models.CharField(blank=True, max_length=250)),
                ('x_main', models.CharField(blank=True, max_length=250)),
                ('y_main', models.CharField(blank=True, max_length=250)),
                ('logic', models.CharField(blank=True, max_length=250)),
                ('inverter', models.CharField(blank=True, max_length=250)),
                ('y_skan', models.CharField(blank=True, max_length=250)),
                ('other', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Samsung',
            },
        ),
        migrations.CreateModel(
            name='Sony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=250)),
                ('power', models.CharField(blank=True, max_length=250)),
                ('main', models.CharField(blank=True, max_length=250)),
                ('t_con', models.CharField(blank=True, max_length=250)),
                ('x_main', models.CharField(blank=True, max_length=250)),
                ('y_main', models.CharField(blank=True, max_length=250)),
                ('logic', models.CharField(blank=True, max_length=250)),
                ('inverter', models.CharField(blank=True, max_length=250)),
                ('y_skan', models.CharField(blank=True, max_length=250)),
                ('other', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Sony',
            },
        ),
        migrations.CreateModel(
            name='Toshiba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=250)),
                ('power', models.CharField(blank=True, max_length=250)),
                ('main', models.CharField(blank=True, max_length=250)),
                ('t_con', models.CharField(blank=True, max_length=250)),
                ('x_main', models.CharField(blank=True, max_length=250)),
                ('y_main', models.CharField(blank=True, max_length=250)),
                ('logic', models.CharField(blank=True, max_length=250)),
                ('inverter', models.CharField(blank=True, max_length=250)),
                ('y_skan', models.CharField(blank=True, max_length=250)),
                ('other', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Toshiba',
            },
        ),
        migrations.CreateModel(
            name='Vityaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=250)),
                ('power', models.CharField(blank=True, max_length=250)),
                ('main', models.CharField(blank=True, max_length=250)),
                ('t_con', models.CharField(blank=True, max_length=250)),
                ('x_main', models.CharField(blank=True, max_length=250)),
                ('y_main', models.CharField(blank=True, max_length=250)),
                ('logic', models.CharField(blank=True, max_length=250)),
                ('inverter', models.CharField(blank=True, max_length=250)),
                ('y_skan', models.CharField(blank=True, max_length=250)),
                ('other', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Vityaz',
            },
        ),
    ]
