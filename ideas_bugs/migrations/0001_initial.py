# Generated by Django 3.1 on 2021-03-31 09:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('work', '0067_product_is_private'),
        ('talent', '0029_person_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('headline', models.CharField(max_length=80)),
                ('idea_type', models.IntegerField(choices=[(0, 'Product Tweak'), (1, 'New Feature'), (2, 'New Capability'), (3, 'Non-Functional Improvement'), (4, 'Other')])),
                ('description', models.TextField()),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='talent.person')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.product')),
                ('related_capability', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='work.capability')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('headline', models.CharField(max_length=80)),
                ('bug_type', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='talent.person')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.product')),
                ('related_capability', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='work.capability')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
