# Generated by Django 3.2.12 on 2022-04-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peerAssessmentApp', '0015_auto_20220420_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcresponse',
            name='mc',
            field=models.CharField(blank=True, choices=[('2', 'Disagree'), ('5', 'Strongly Agree'), ('3', 'Neutral'), ('4', 'Agree'), ('1', 'Strongly Disagree')], max_length=20),
        ),
    ]