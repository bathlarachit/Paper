# Generated by Django 3.0.3 on 2021-01-31 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0002_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='TF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('ans', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=20)),
                ('marks', models.PositiveIntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.Exam')),
            ],
        ),
    ]
