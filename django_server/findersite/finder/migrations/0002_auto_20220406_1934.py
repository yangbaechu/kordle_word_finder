# Generated by Django 3.2.12 on 2022-04-06 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='letter1',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='word',
            name='letter2',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='word',
            name='letter3',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='word',
            name='letter4',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='word',
            name='letter5',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='word',
            name='letter6',
            field=models.CharField(default='', max_length=5),
        ),
    ]
