# Generated by Django 4.0.5 on 2022-06-05 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('user_pw', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('school_name', models.CharField(max_length=100)),
                ('grade_number', models.IntegerField(default=1)),
                ('class_number', models.IntegerField(default=1)),
                ('student_number', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
