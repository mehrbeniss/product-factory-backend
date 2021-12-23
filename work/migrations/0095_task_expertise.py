# Generated by Django 3.1 on 2021-11-26 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0094_expertise'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='expertise',
            field=models.ManyToManyField(related_name='task_expertise', to='work.Expertise'),
        ),
    ]
