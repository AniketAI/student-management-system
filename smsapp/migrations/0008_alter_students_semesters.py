# Generated by Django 4.1.2 on 2022-10-20 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0007_alter_students_semesters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='semesters',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsapp.semesters'),
        ),
    ]