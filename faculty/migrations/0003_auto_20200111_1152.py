# Generated by Django 3.0 on 2020-01-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_faculty_cnfrmpassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='facultyid',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
