# Generated by Django 2.1.5 on 2019-02-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190210_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mentors',
            field=models.ManyToManyField(related_name='_member_mentors_+', to='api.Member'),
        ),
    ]