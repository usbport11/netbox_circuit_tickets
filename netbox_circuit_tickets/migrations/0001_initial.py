# Generated by Django 4.1.5 on 2023-04-13 07:12

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extras', '0084_staging'),
        ('circuits', '0041_standardize_description_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='CircuitTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=30)),
                ('start', models.DateTimeField(max_length=100)),
                ('end', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('acknowledged', models.BooleanField(blank=True, default=False, null=True)),
                ('comments', models.TextField(blank=True)),
                ('circuit', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='circuits.circuit')),
                ('provider', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='circuits.provider')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
