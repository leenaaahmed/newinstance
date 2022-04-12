# Generated by Django 3.2.12 on 2022-04-05 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peerAssessmentApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cassess',
            name='due_date',
            field=models.DateField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='cassess',
            name='publish_date',
            field=models.DateField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='siteusers',
            name='type',
            field=models.CharField(blank=True, choices=[('pro', 'professor'), ('stu', 'student')], default=None, max_length=3, null=True),
        ),
    ]