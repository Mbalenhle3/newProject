# Generated by Django 5.1.1 on 2024-09-30 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gym', '0012_profile_first_name_profile_is_community_member_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_community_member',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='residence',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='student_number',
        ),
    ]
