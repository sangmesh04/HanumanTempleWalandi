# Generated by Django 3.2.8 on 2021-11-02 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_first_name', models.CharField(max_length=100)),
                ('feedback_last_name', models.CharField(max_length=100)),
                ('feedback_mobile_number', models.CharField(max_length=12)),
                ('feedback_text', models.TextField()),
                ('feedback_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
