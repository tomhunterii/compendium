# Generated by Django 3.2.8 on 2022-01-20 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20220119_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column='Name', max_length=60, null=True)),
                ('desc', models.CharField(blank=True, db_column='Description', max_length=260, null=True)),
                ('category', models.CharField(blank=True, db_column='Category', max_length=60, null=True)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=60, null=True)),
                ('ac', models.CharField(blank=True, db_column='Armor Class', max_length=60, null=True)),
                ('stealth', models.CharField(blank=True, db_column='stealth', max_length=60, null=True)),
                ('str_req', models.CharField(blank=True, db_column='Strength Requirement', max_length=60, null=True)),
                ('cost', models.CharField(blank=True, db_column='Cost', max_length=60, null=True)),
                ('modifier', models.IntegerField(blank=True, db_column='Modifier', max_length=2, null=True)),
                ('weight', models.IntegerField(blank=True, db_column='Weight', max_length=60, null=True)),
                ('rarity', models.IntegerField(blank=True, db_column='Rarity', max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Char_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('desc', models.CharField(max_length=800)),
                ('hit_die', models.CharField(max_length=60)),
                ('primary_ability', models.CharField(max_length=60)),
                ('saving_throw_prof', models.CharField(max_length=60)),
                ('armor_wep_prof', models.CharField(max_length=60)),
                ('features', models.CharField(max_length=800)),
                ('subclasses', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Char_race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('desc', models.CharField(max_length=800)),
                ('traits', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column='Name', max_length=60, null=True)),
                ('desc', models.CharField(blank=True, db_column='Description', max_length=260, null=True)),
                ('cost', models.CharField(blank=True, db_column='Cost', max_length=60, null=True)),
                ('property', models.CharField(blank=True, db_column='Properties', max_length=60, null=True)),
                ('weight', models.IntegerField(blank=True, db_column='Weight', max_length=60, null=True)),
                ('rarity', models.IntegerField(blank=True, db_column='Rarity', max_length=60, null=True)),
                ('modifiers', models.IntegerField(blank=True, db_column='Modifiers', max_length=60, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='weapon_desc',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='weapon_dmg_1',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='weapon_dmg_2',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='weapon_modifier',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='weapon_name',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='weapon_property_1',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='weapon_property_2',
        ),
        migrations.AddField(
            model_name='weapon',
            name='category',
            field=models.CharField(blank=True, db_column='Category', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='weapon',
            name='cost',
            field=models.CharField(blank=True, db_column='Cost', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='weapon',
            name='desc',
            field=models.CharField(blank=True, db_column='Description', max_length=260, null=True),
        ),
        migrations.AddField(
            model_name='weapon',
            name='dmg',
            field=models.CharField(blank=True, db_column='Damage', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='weapon',
            name='modifier',
            field=models.IntegerField(blank=True, db_column='Modifier', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='weapon',
            name='name',
            field=models.CharField(blank=True, db_column='Name', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='weapon',
            name='property',
            field=models.CharField(blank=True, db_column='Properties', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='weapon',
            name='rarity',
            field=models.IntegerField(blank=True, db_column='Rarity', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='weapon',
            name='type',
            field=models.CharField(blank=True, db_column='Type', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='weapon',
            name='weight',
            field=models.IntegerField(blank=True, db_column='Weight', max_length=60, null=True),
        ),
    ]
