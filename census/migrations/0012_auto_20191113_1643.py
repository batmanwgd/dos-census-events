# Generated by Django 2.2.7 on 2019-11-14 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0011_auto_20191112_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='approval_status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved')], default='PENDING', max_length=20),
        ),
    ]