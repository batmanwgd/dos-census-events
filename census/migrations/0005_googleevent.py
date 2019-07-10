# Generated by Django 2.2.1 on 2019-06-12 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0004_auto_20190511_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_calendar_id', models.CharField(max_length=100)),
                ('published', models.DateTimeField(help_text='Time when the Event was published')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='census.Event')),
            ],
        ),
    ]