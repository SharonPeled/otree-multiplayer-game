from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import numpy as np

author = 'Plonsky and Roth'

doc = """
23 Jan 2020.  
Entrance Screen
"""

class Constants(BaseConstants):
    name_in_url = 'NashTEnt'
    players_per_group = None
    num_rounds = 1
    show_up_fee=0
    endowment = 0

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    #Record participants age
    age = models.PositiveIntegerField(
        verbose_name='What is your age?',
        min=13, max=125)

    #Record participants gender
    gender = models.CharField(
        choices=['Male', 'Female','Other'],
        verbose_name='What is your gender?',
        widget=widgets.RadioSelect())
