# Generated by Django 3.0.6 on 2020-06-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_auto_20200603_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(default=True, max_length=60, unique=True),
        ),
    ]