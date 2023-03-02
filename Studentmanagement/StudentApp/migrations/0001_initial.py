# Generated by Django 4.1.4 on 2023-01-29 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stud_Name', models.CharField(max_length=50)),
                ('Stud_Age', models.IntegerField()),
                ('Stud_Phno', models.BigIntegerField()),
                ('Stud_City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.city')),
                ('Stud_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.course')),
            ],
        ),
    ]
