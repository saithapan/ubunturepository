# Generated by Django 3.0.7 on 2021-02-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_mark_test_student_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
                ('test_region', models.CharField(max_length=100)),
                ('test_country', models.CharField(max_length=100)),
                ('test_village', models.CharField(max_length=100)),
            ],
        ),
    ]
