# Generated by Django 2.1.5 on 2019-02-09 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190209_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='m_id',
            field=models.CharField(default='null', max_length=10),
        ),
    ]
