# Generated by Django 3.2.8 on 2022-01-20 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20220120_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='char_race',
            name='desc',
            field=models.CharField(blank=True, db_column='Description', max_length=16000, null=True),
        ),
    ]
