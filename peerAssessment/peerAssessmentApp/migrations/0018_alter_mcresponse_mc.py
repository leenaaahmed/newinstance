# Generated by Django 4.0.3 on 2022-04-20 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peerAssessmentApp', '0017_rename_user_registry_admin_course_access_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcresponse',
            name='mc',
            field=models.CharField(blank=True, choices=[('5', 'Strongly Agree'), ('1', 'Strongly Disagree'), ('4', 'Agree'), ('2', 'Disagree'), ('3', 'Neutral')], max_length=20),
        ),
    ]