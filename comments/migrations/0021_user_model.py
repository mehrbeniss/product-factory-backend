# Generated by Django 3.1 on 2021-06-15 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0032_user_model'),
        ('comments', '0020_capabilitycomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bugcomment',
            name='person',
        ),
        migrations.RemoveField(
            model_name='capabilitycomment',
            name='person',
        ),
        migrations.RemoveField(
            model_name='ideacomment',
            name='person',
        ),
        migrations.RemoveField(
            model_name='taskcomment',
            name='person',
        ),
        migrations.AddField(
            model_name='bugcomment',
            name='customer_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent.person'),
        ),
        migrations.AddField(
            model_name='capabilitycomment',
            name='customer_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent.person'),
        ),
        migrations.AddField(
            model_name='ideacomment',
            name='customer_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent.person'),
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='customer_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talent.person'),
        ),
    ]
