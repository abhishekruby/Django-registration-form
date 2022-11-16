# Generated by Django 4.1.3 on 2022-11-16 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='students_Photo/')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=120)),
                ('degree', models.CharField(choices=[('bca', 'BCA'), ('b-tech', 'B-Tech'), ('bsc', 'BSC')], max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
        ),
    ]