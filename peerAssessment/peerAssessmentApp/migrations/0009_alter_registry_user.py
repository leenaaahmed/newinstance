# Generated by Django 3.2.12 on 2022-03-30 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peerAssessmentApp', '0008_alter_siteusers_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peerAssessmentApp.siteusers'),
        ),
    ]
