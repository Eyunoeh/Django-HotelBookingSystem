# Generated by Django 4.1.3 on 2022-12-24 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='id',
        ),
        migrations.AlterField(
            model_name='checkout',
            name='code',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
