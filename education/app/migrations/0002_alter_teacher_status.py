# Generated by Django 5.0.3 on 2024-05-30 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='status',
            field=models.CharField(max_length=255, verbose_name='Teacher Status'),
        ),
    ]
