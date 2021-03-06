# Generated by Django 3.0 on 2020-01-14 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_auto_20200111_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='cnfrmpassword',
        ),
        migrations.AlterField(
            model_name='faculty',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='dob',
            field=models.DateField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='email',
            field=models.EmailField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='joiningdate',
            field=models.CharField(max_length=20),
        ),
    ]
