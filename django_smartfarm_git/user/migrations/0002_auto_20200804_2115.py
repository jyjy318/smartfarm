# Generated by Django 2.0.13 on 2020-08-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todaytalk',
            name='talk',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
