# Generated by Django 2.2.3 on 2019-09-15 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20190911_0616'),
        ('schools', '0001_initial'),
        ('students', '0002_auto_20190915_0301'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMigration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academicyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.AcademicYear')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.ClassRoom')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
    ]
