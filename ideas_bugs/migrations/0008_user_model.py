# Generated by Django 3.1 on 2021-06-15 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0032_user_model'),
        ('ideas_bugs', '0007_user_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bugvote',
            name='person',
        ),
        migrations.RemoveField(
            model_name='ideavote',
            name='person',
        ),
        migrations.AddField(
            model_name='bugvote',
            name='customer_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='talent.person'),
        ),
        migrations.AddField(
            model_name='ideavote',
            name='customer_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='talent.person'),
        ),
    ]
