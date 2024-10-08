# Generated by Django 5.1.1 on 2024-09-29 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gym', '0005_paymentprocedure'),
    ]

    operations = [
        migrations.CreateModel(
            name='GymRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
