# Generated by Django 5.1.1 on 2024-09-27 14:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gym', '0003_alter_choice_question'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveyresponse',
            old_name='created_at',
            new_name='submitted_at',
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
