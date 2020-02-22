# Generated by Django 3.0.3 on 2020-02-22 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_options', models.CharField(max_length=100)),
                ('right_answer', models.CharField(max_length=100)),
                ('is_repeated', models.BooleanField(default=False, help_text='Is this a repeated question?')),
                ('is_correct', models.BooleanField(default=False, help_text='Is this a correct answer?')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('level', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('level_flag', models.IntegerField(default=1)),
                ('mcq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Answers')),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='ques',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Questions'),
        ),
    ]
