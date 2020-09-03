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
from global_utilities import utils

author = 'Sharon Peled'

doc = """
Timer to the game
"""


class Constants(BaseConstants):
    name_in_url = 'game_timer'
    players_per_group = None
    num_rounds = 1
    penalty_for_first_phase = utils.GlobalConstant.penalty_for_first_phase
    basic_payment = utils.GlobalConstant.basic_payment
    experiment_starting_time = utils.GlobalConstant.experiment_starting_time
    completion_code = utils.GlobalConstant.completion_code
    reminder_time = utils.GlobalConstant.reminder_time
    sender_email = utils.GlobalConstant.sender_email  # email to send emails from
    sender_email_password = utils.GlobalConstant.sender_email_password
    email_title = utils.GlobalConstant.email_title
    email_body_sentences = utils.GlobalConstant.email_body_sentences



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    email = models.StringField(initial="", blank=True)
    is_player_wants_to_proceed = models.BooleanField(initial=False, blank=True)
    is_player_wants_reminder = models.BooleanField(initial=False, blank=True)
