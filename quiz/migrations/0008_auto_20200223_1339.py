# Generated by Django 2.2.3 on 2020-02-23 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20200223_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level_flag',
            field=models.CharField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, max_length=5),
        ),
    ]
