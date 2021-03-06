# Generated by Django 3.2.7 on 2021-12-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=12)),
                ('confirmpassword', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=122)),
                ('dob', models.CharField(max_length=12)),
                ('gender', models.CharField(max_length=1)),
                ('city', models.CharField(max_length=10)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='index',
        ),
    ]
