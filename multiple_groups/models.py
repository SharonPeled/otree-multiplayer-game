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
import time
import math
author = 'Sharon Peled'

doc = """
Experiment that guarantees multiple active players
"""


class Constants(BaseConstants):
    name_in_url = 'multiple_groups'
    players_per_group = None
    num_rounds = 1
    seconds_to_passive = 20
    passive_allowed_time = 20
    group_size = 5
    active_players_per_group = 3 # number of players per group
    tail_rate=0.95 # percentage of participants who chose Tails to get the bonus
    high_pay=0.40
    low_pay=0.20
    q1_reduce_factor = 1/4
    q2_reduce_factor = 3/4


class Subsession(BaseSubsession):
    group_number = models.IntegerField(initial=1)
    tot_playing_players = models.IntegerField(initial=0)

    # def creating_session(self):

    def group_by_arrival_time_method(self, waiting_players):
        # print(waiting_players)
        # not enough spots/links to form a group
        if Constants.group_size - self.tot_playing_players < Constants.active_players_per_group :
            self.remove_players(waiting_players)
            return waiting_players
        active_players = [w for w in waiting_players if w.is_active]
        passive_players = [w for w in waiting_players if not w.is_active]
        # not enough active players to form a group
        if len(active_players) < Constants.active_players_per_group:
            # if all players arrived and unable to form a group with the current players
            if self.tot_playing_players+len(waiting_players) == Constants.group_size:
                self.remove_players(waiting_players)
                return waiting_players
            # self.swith_to_be_switched(waiting_players)
            return None # not enough players to create a game
        self.set_game_number(active_players,self.group_number)
        self.group_number += 1
        self.force_passive(passive_players)
        self.tot_playing_players += len(active_players)
        return active_players # active players will move to the actual game

    def remove_players(self,players):
        for player in players:
            player.is_in = False

    def set_game_number(self,active_players,group_num):
        for player in active_players:
            player.group_num = group_num

    def force_passive(self,players):
        for player in players:
            player.force_passive = True



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # general info
    age = models.PositiveIntegerField(
        verbose_name='What is your age?',
        min=13, max=125)
    gender = models.CharField(
        choices=['Male', 'Female','Other'],
        verbose_name='What is your gender?',
        widget=widgets.RadioSelect())
    q1_answer = models.StringField(
        choices=['0', '10', '20', '30', '40'],
        widget=widgets.RadioSelect())
    q2_answer = models.StringField(
        choices=['0', '10', '20', '30', '40'],
        widget=widgets.RadioSelect())
    # game info
    play = models.BooleanField()


    is_active = models.BooleanField(initial=False) # if the player is active or not
    is_in = models.BooleanField(initial=True) # if the player can enter a game
    group_num = models.IntegerField(initial=0) # number of game the player has entered (0 - didn't enter a game at all)
    force_passive = models.BooleanField(initial=True)
    beg_passive_time = models.FloatField(initial=time.time())

    def set_status(self):
        if self.force_passive:
            self.is_active = False
            self.force_passive = False
            self.beg_passive_time = time.time()
            return self.is_active
        if not self.is_active: # was passive and come to get change
            # he was passive more time then allowed - should remain passive, in the next reload he'd be changed to active.
            if Constants.passive_allowed_time <= (time.time() - self.beg_passive_time):
                self.beg_passive_time = time.time()
                return self.is_active
        self.is_active = not self.is_active
        self.beg_passive_time = time.time()
        return self.is_active
