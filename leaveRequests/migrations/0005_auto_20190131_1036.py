# Generated by Django 2.1.4 on 2019-01-31 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaveRequests', '0004_leaverequest_reason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaverequest',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='manager',
        ),
        migrations.DeleteModel(
            name='LeaveRequest',
        ),
    ]
