# Generated by Django 2.1.4 on 2019-01-13 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalcHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('first', models.IntegerField()),
                ('second', models.IntegerField()),
                ('result', models.IntegerField()),
            ],
        ),
    ]
