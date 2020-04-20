from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Philipp Chapkovski, HSE-Moscow, chapkovski@gmail.com'

doc = """
An app that matches only active players.
"""


class Constants(BaseConstants):
    name_in_url = 'match'
    players_per_group = None
    num_rounds = 1
    seconds_to_passive = 5
    group_size = 3

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    active = models.BooleanField(initial=True)
