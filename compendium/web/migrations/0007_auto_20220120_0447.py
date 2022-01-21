# Generated by Django 3.2.8 on 2022-01-20 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20220120_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='char_race',
            name='size',
            field=models.CharField(blank=True, db_column='Size', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='char_race',
            name='speed',
            field=models.IntegerField(blank=True, db_column='Speed', null=True),
        ),
        migrations.AlterField(
            model_name='char_class',
            name='desc',
            field=models.CharField(max_length=6000),
        ),
        migrations.AlterField(
            model_name='char_class',
            name='features',
            field=models.CharField(max_length=6000),
        ),
        migrations.AlterField(
            model_name='char_class',
            name='subclasses',
            field=models.CharField(max_length=6000),
        ),
        migrations.AlterField(
            model_name='char_race',
            name='desc',
            field=models.CharField(blank=True, db_column='Description', max_length=6000, null=True),
        ),
        migrations.AlterField(
            model_name='char_race',
            name='name',
            field=models.CharField(blank=True, db_column='Name', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='char_race',
            name='traits',
            field=models.CharField(blank=True, db_column='Traits', max_length=6000, null=True),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='dmg',
            field=models.CharField(blank=True, db_column='Damage', max_length=60, null=True),
        ),
    ]