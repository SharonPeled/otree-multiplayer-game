# Generated by Django 2.2.4 on 2020-04-06 11:00

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('number_entrants', otree.db.models.IntegerField(null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nash_t_group', to='otree.Session')),
            ],
            options={
                'db_table': 'Nash_T_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('paying_round', otree.db.models.IntegerField(null=True)),
                ('condition', otree.db.models.IntegerField(null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nash_t_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'Nash_T_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('age', otree.db.models.PositiveIntegerField(null=True, verbose_name='What is your age?')),
                ('gender', otree.db.models.StringField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10000, null=True, verbose_name='What is your gender?')),
                ('und_quest1', otree.db.models.StringField(choices=[('0', '0'), ('10', '10'), ('20', '20'), ('30', '30'), ('40', '40')], max_length=10000, null=True)),
                ('und_quest2', otree.db.models.StringField(choices=[('0', '0'), ('10', '10'), ('20', '20'), ('30', '30'), ('40', '40')], max_length=10000, null=True)),
                ('cond', otree.db.models.FloatField(null=True)),
                ('timeout_submission', otree.db.models.IntegerField(null=True)),
                ('penalty', otree.db.models.FloatField(null=True)),
                ('play_in', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Nash_T.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nash_t_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nash_t_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nash_T.Subsession')),
            ],
            options={
                'db_table': 'Nash_T_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nash_T.Subsession'),
        ),
    ]
