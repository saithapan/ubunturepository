# Generated by Django 3.0.7 on 2021-02-19 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_task_list2'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_test',
            fields=[
                ('stid', models.IntegerField(primary_key=True, serialize=False)),
                ('stdname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='mark_test',
            fields=[
                ('marks_id', models.IntegerField(primary_key=True, serialize=False)),
                ('social', models.CharField(max_length=100)),
                ('science', models.CharField(max_length=100)),
                ('maths', models.CharField(max_length=100)),
                ('stid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='test_app.student_test')),
            ],
        ),
    ]
