# Generated by Django 3.2.8 on 2022-01-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20220119_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weapon',
            old_name='weapon_type',
            new_name='weapon_property_1',
        ),
        migrations.AddField(
            model_name='weapon',
            name='weapon_modifier',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='weapon',
            name='weapon_property_2',
            field=models.CharField(choices=[('1', 'Heavy'), ('2', 'Finese'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='1', max_length=20),
        ),
    ]
