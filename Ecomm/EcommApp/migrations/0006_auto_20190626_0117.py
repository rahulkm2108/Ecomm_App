# Generated by Django 2.2.2 on 2019-06-25 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcommApp', '0005_auto_20190626_0116'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categories',
            new_name='category',
        ),
    ]