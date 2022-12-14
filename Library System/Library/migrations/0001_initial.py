# Generated by Django 3.1.6 on 2021-02-09 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('Book_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Book_Title', models.CharField(max_length=100)),
                ('Book_Author', models.CharField(max_length=50)),
                ('Book_Pages', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_RollNo', models.CharField(max_length=50)),
                ('Std_Name', models.CharField(max_length=50)),
                ('Std_Address', models.CharField(max_length=100)),
                ('std_StudyProgram', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Issue_Date', models.DateField()),
                ('Return_Date', models.DateField()),
                ('Remarks', models.CharField(max_length=50)),
                ('Book_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.book')),
                ('std_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.student')),
            ],
        ),
    ]
