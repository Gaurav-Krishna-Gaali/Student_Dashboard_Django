# Generated by Django 4.2.2 on 2023-06-11 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_students_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_numer',
            new_name='student_number',
        ),
    ]
