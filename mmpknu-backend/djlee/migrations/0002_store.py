# Generated by Django 2.0.13 on 2019-07-15 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djlee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GPSX', models.CharField(max_length=50)),
                ('GPSY', models.CharField(max_length=50)),
                ('LARG_CATE', models.CharField(max_length=50)),
                ('MID_CATE', models.CharField(max_length=50)),
                ('SMALL_CATE', models.CharField(max_length=50)),
                ('NAME', models.CharField(max_length=50)),
                ('URL', models.CharField(max_length=50)),
            ],
        ),
    ]
