# Generated by Django 3.2.9 on 2021-11-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_userinfo_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=2),
        ),
    ]
