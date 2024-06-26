# Generated by Django 5.0.3 on 2024-05-29 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Course Name')),
                ('description', models.TextField(verbose_name='Course Description')),
                ('price', models.IntegerField(verbose_name='Course Price')),
                ('lifetime', models.IntegerField(verbose_name='Course Lifetime')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Teacher Full Name')),
                ('status', models.IntegerField(verbose_name='Teacher Status')),
                ('experience', models.IntegerField(verbose_name='Teacher Experience')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course', verbose_name='Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Student Full Name')),
                ('phone', models.CharField(max_length=255, verbose_name='Student Phone')),
                ('email', models.CharField(max_length=255, verbose_name='Student Email')),
                ('parentsphone', models.CharField(max_length=255, verbose_name='Parents Phone')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course', verbose_name='Course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teacher', verbose_name='Teacher')),
            ],
        ),
    ]
