# Generated by Django 4.0.3 on 2022-04-19 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peerAssessmentApp', '0014_auto_20220415_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registry',
            old_name='User',
            new_name='professor',
        ),
        migrations.AlterField(
            model_name='mcresponse',
            name='mc',
            field=models.CharField(blank=True, choices=[('5', 'Strongly Agree'), ('2', 'Disagree'), ('3', 'Neutral'), ('1', 'Strongly Disagree'), ('4', 'Agree')], max_length=20),
        ),
    ]
