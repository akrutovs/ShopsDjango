# Generated by Django 4.1.1 on 2022-09-23 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '0002_alter_city_options_alter_city_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название улицы')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.city', verbose_name='id города')),
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': 'Улицы',
            },
        ),
    ]
