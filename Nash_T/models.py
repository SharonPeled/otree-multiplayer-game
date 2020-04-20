from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import numpy as np

author = 'Plonsky and Roth'

doc = """
23 Jan 2020.  
"""

class Constants(BaseConstants):
    name_in_url = 'NashT'
    players_per_group = 3
    num_rounds = 1
    show_up_fee=0
    endowment = 0
    first_rounds=1
    time_to_response_first_rounds=60
    time_to_response = 300
    condition=1
    t_rate=0.95 #percent of participants to enter the game to get the bonus
    high_pay=0.40
    low_pay=0.20
    payratio=100.0
    convert_rate=1 # 1 point equal 1 $ cent

class Subsession(BaseSubsession):

    paying_round = models.IntegerField()
    condition = models.IntegerField()  #1: IN/OUT 2:OUT/IN

    def creating_session(self):
        if self.round_number == 1:
            self.condition = random.randint(1, 2)
            if Constants.num_rounds > 1:
                self.paying_round = random.randint(1, Constants.num_rounds)
            else:
                self.paying_round = 1
            self.session.vars['paying_round'] = self.paying_round

class Group(BaseGroup):

    number_entrants = models.IntegerField()  # how many participants entered

    def set_payoffs(self):
        self.number_entrants = 0
        players = self.get_players()

        for p in players:
            if p.play_in == True:
                self.number_entrants = self.number_entrants + 1

        for p in players:
            # print('player_role_is',self.get_player_by_role('poster').poster_choice)
            # print('player_role_is',self.get_player_by_role('poster'))
            if p.play_in == False:
                p.payoff = Constants.low_pay - p.penalty
            else:  #entered
                if self.number_entrants >= int(Constants.players_per_group * Constants.t_rate):  #SUCCESS
                    p.payoff = Constants.high_pay - p.penalty
                else:
                    p.payoff = 0 - p.penalty
        return {
            'number_entrants': self.number_entrants,
            'play_pay': p.payoff
        }


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

    # Whether participant understood the Instructions
    und_quest1 = models.StringField(
        choices=['0', '10', '20', '30', '40'],
        widget=widgets.RadioSelect())
    und_quest2 = models.StringField(
        choices=['0', '10', '20', '30', '40'],
        widget=widgets.RadioSelect())

    #Number of entrants into the game
    #number_entrants=models.IntegerField()

    cond=models.FloatField() ##condition


    timeout_submission = models.IntegerField()
    penalty = models.FloatField()

    play_in = models.BooleanField()

    def play_in_choices(self):
        if self.subsession.in_round(1).condition < 2:
            return [[True, 'TAILS'], [False, 'HEADS']]
        else:
            return [[False, 'HEADS'], [True, 'TAILS']]

    #def TFT_P1(self):
    #    if self.round_number>1:
    #            if other_player.in_round(self.round_number-1).play_left==True:
    #                return True
    #            else:
    #                return False
    #def TFT_P2(self):
    #    return roles[self.id_in_group - 1]