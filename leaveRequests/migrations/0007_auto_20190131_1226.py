# Generated by Django 2.1.4 on 2019-01-31 12:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leaveRequests', '0006_leaverequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
