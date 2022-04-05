# Generated by Django 3.2.12 on 2022-03-30 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('peerAssessmentApp', '0009_alter_registry_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]