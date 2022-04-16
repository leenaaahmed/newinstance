# Generated by Django 3.2.12 on 2022-04-15 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peerAssessmentApp', '0010_auto_20220412_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcresponse',
            name='responder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='peerAssessmentApp.siteusers'),
        ),
        migrations.AddField(
            model_name='response',
            name='responder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='peerAssessmentApp.siteusers'),
        ),
        migrations.AlterField(
            model_name='mcresponse',
            name='mc',
            field=models.CharField(blank=True, choices=[('5', 'Strongly Agree'), ('3', 'Neutral'), ('4', 'Agree'), ('1', 'Strongly Disagree'), ('2', 'Disagree')], max_length=20),
        ),
    ]