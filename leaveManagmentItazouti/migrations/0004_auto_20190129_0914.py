# Generated by Django 2.1.5 on 2019-01-29 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveManagmentItazouti', '0003_auto_20190129_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavetype',
            name='daysNumber',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
