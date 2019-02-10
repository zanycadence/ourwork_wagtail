# Generated by Django 2.1.5 on 2019-02-10 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_member_m_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Member'),
        ),
        migrations.AddField(
            model_name='member',
            name='mentors',
            field=models.ManyToManyField(related_name='_member_mentors_+', to='api.Member'),
        ),
    ]
