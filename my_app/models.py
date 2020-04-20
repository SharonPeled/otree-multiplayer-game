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

author = 'Sharon Peled'

doc = """
Experiment that guarantees multiple active players
"""


class Constants(BaseConstants):
    name_in_url = 'my_app'
    players_per_group = None
    num_rounds = 1
    seconds_to_passive = 5
    group_size = 5
    active_players_size = 3


class Subsession(BaseSubsession):
    is_group_formed = models.BooleanField(initial=False)

    def creating_session(self):
        self.is_group_formed = False

    def group_by_arrival_time_method(self, waiting_players):
        if self.is_group_formed:
            self.update_users_potential(waiting_players)
            return waiting_players
        active_players = [w for w in waiting_players if w.is_player_active]
        passive_players = [w for w in waiting_players if not w.is_player_active]
        if len(active_players) < Constants.active_players_size:
            if len(waiting_players) == Constants.group_size: # if all players arrived and still not enough active ones
                self.update_users_potential(waiting_players)
                return waiting_players
            return None # not enough players to create a game
        self.is_group_formed = True
        self.update_users_potential(passive_players)
        return waiting_players # the active players will move to the actuall game and the passive ones to game over

    def update_users_potential(self,players):
        for player in players:
            player.is_player_in = False


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    is_player_active = models.BooleanField(initial=True)
    is_player_in = models.BooleanField(initial=True)

    def set_status(self):
        self.is_player_active = not self.is_player_active
        return self.is_player_active
