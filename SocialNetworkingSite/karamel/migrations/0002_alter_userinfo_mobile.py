# Generated by Django 4.0.2 on 2022-02-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karamel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='mobile',
            field=models.IntegerField(max_length=12),
        ),
    ]
