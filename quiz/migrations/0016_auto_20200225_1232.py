# Generated by Django 2.2.3 on 2020-02-25 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_level_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='category_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Category'),
        ),
    ]
