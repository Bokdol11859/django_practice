# Generated by Django 4.0.4 on 2022-05-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_on',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]
