# Generated by Django 3.2.8 on 2021-11-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_donors_donor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='donoration_time',
            field=models.CharField(max_length=50),
        ),
    ]