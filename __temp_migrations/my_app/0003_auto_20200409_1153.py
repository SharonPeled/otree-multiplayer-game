# Generated by Django 2.2.4 on 2020-04-09 08:53

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_player_is_player_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='is_player_active',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
    ]
