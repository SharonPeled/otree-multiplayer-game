from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from global_utilities.utils import GlobalConstant

author = 'Sharon Peled'

doc = """
Pages and things to be done prior to the actual multi-player game.
"""


class Constants(BaseConstants):
    name_in_url = 'Heads/Tails_Game_instructions'
    players_per_group = None
    num_rounds = 1
    active_players_per_group = GlobalConstant.active_players_per_group
    tail_rate = GlobalConstant.tail_rate
    high_pay = GlobalConstant.high_pay
    low_pay = GlobalConstant.low_pay
    basic_payment = GlobalConstant.basic_payment
    q1_reduce_factor = GlobalConstant.q1_reduce_factor
    q2_reduce_factor = GlobalConstant.q2_reduce_factor



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.PositiveIntegerField(
        verbose_name='What is your age?',
        min=13, max=125)
    gender = models.CharField(
        choices=['Male', 'Female', 'Other'],
        verbose_name='What is your gender?',
        widget=widgets.RadioSelect())
    q1_answer = models.StringField(
        choices=['0', '10', '20', '30', '40'],
        widget=widgets.RadioSelect())
    q2_answer = models.StringField(
        choices=['0', '10', '20', '30', '40'],
        widget=widgets.RadioSelect())
