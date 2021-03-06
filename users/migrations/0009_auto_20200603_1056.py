# Generated by Django 3.0.6 on 2020-06-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200601_0749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersdata',
            old_name='name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='usersdata',
            old_name='gender',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='usersdata',
            old_name='username',
            new_name='lastname',
        ),
        migrations.AddField(
            model_name='usersdata',
            name='timezone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
