# Generated by Django 3.2.9 on 2022-02-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chp_look_up', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curietocommonname',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='genetopathway',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pathwaytogene',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]