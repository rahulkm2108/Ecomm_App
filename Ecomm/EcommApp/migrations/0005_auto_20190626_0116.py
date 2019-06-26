# Generated by Django 2.2.2 on 2019-06-25 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommApp', '0004_auto_20190626_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryId', models.IntegerField()),
                ('CategoryName', models.CharField(max_length=255)),
                ('Discription', models.CharField(max_length=1000)),
                ('Picture', models.CharField(max_length=500)),
                ('Active', models.BooleanField()),
                ('Created', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='category',
        ),
    ]