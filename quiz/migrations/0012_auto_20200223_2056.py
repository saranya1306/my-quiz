# Generated by Django 2.2.3 on 2020-02-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20200223_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='level_no',
            field=models.IntegerField(blank=True, choices=[(1, 'Hi'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]