# Generated by Django 3.2.8 on 2022-01-19 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon_name', models.CharField(max_length=50)),
                ('weapon_desc', models.CharField(max_length=250)),
                ('weapon_dmg', models.CharField(max_length=10)),
                ('weapon_type', models.CharField(max_length=10)),
            ],
        ),
    ]