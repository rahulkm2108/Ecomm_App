# Generated by Django 2.2.2 on 2019-06-25 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryId', models.IntegerField()),
                ('CategoryName', models.CharField(max_length=255)),
                ('Discription', models.CharField(max_length=2000)),
                ('Picture', models.CharField(max_length=500)),
                ('Active', models.BooleanField()),
                ('Created', models.DateTimeField()),
            ],
        ),
    ]
