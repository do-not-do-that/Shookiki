# Generated by Django 3.1.7 on 2021-05-09 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0003_useraccount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]