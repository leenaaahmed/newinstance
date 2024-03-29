# Generated by Django 4.0.3 on 2022-04-20 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('peerAssessmentApp', '0016_alter_mcresponse_mc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registry',
            old_name='User',
            new_name='admin',
        ),
        migrations.AddField(
            model_name='course',
            name='access_code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='admins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='students', to='peerAssessmentApp.siteusers'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='mcresponse',
            name='mc',
            field=models.CharField(blank=True, choices=[('4', 'Agree'), ('2', 'Disagree'), ('5', 'Strongly Agree'), ('1', 'Strongly Disagree'), ('3', 'Neutral')], max_length=20),
        ),
        migrations.AlterField(
            model_name='submission',
            name='reviewee',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewee', to='peerAssessmentApp.siteusers'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='satus',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.DeleteModel(
            name='Enrollment',
        ),
    ]
