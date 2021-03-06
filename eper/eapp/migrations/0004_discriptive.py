# Generated by Django 3.0.3 on 2021-01-31 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0003_tf'),
    ]

    operations = [
        migrations.CreateModel(
            name='discriptive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('marks', models.PositiveIntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.Exam')),
            ],
        ),
    ]
