# Generated by Django 3.2.12 on 2022-04-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peerAssessmentApp', '0006_auto_20220412_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcresponse',
            name='mc',
            field=models.CharField(blank=True, choices=[('4', 'Agree'), ('1', 'Strongly Disagree'), ('5', 'Strongly Agree'), ('2', 'Disagree'), ('3', 'Neutral')], max_length=20),
        ),
    ]
