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
from global_utilities.utils import GlobalConstant
import random

author = 'Sharon Peled'

doc = """
Participants waiting room that guarantees that only when enough active participants are available
 they move together to the next phase of the experiment.
"""

class Constants(BaseConstants):
    name_in_url = 'Heads/Tails_Game_WaitPage'
    players_per_group = None
    num_rounds = 1
    seconds_to_passive = GlobalConstant.seconds_to_passive
    passive_allowed_time = GlobalConstant.passive_allowed_time
    group_size = GlobalConstant.group_size
    active_players_per_group = GlobalConstant.active_players_per_group
    completion_code = GlobalConstant.completion_code
    basic_payment = GlobalConstant.basic_payment
    activeness_waiting_threshold = GlobalConstant.activeness_waiting_threshold
    waiting_time_threshold = GlobalConstant.waiting_time_threshold
    penalty = GlobalConstant.penalty

class Subsession(BaseSubsession):
    game_number = models.IntegerField(initial=1)
    tot_players_proceed = models.IntegerField(initial=0) # number of users that proceed from the wait page (to game/to end)

    # possible solution: add refreshes with force passive/active every 30 seconds
    def group_by_arrival_time_method(self, waiting_players):
        waiting_players = sorted(waiting_players, key=Subsession.sort_by_entrace)
        users_to_game = [] # users to move to the game
        users_to_end = [] # users to move to end
        active_players = [player for player in waiting_players if player.is_active][:Constants.active_players_per_group]
        # enough active players to form a game
        if len(active_players) == Constants.active_players_per_group:
            self.set_game(active_players, self.game_number)
            # rest players are forced to be passive
            self.force_passive([player for player in waiting_players if player not in active_players])
            users_to_game += active_players
        rest_players = [player for player in waiting_players if player not in users_to_game] # players who don't move to game
        # if all users playing are waiting (but arrived) OR there aren't enough links to form a group
        if (self.tot_players_proceed + len(waiting_players) == Constants.group_size) \
                or (Constants.group_size - self.tot_players_proceed < Constants.active_players_per_group):
            self.remove_players(rest_players)
            users_to_end += rest_players
        else: # not everyone is here, the waiting page is still on
            # players who are too long in the waiting room
            waited_too_long_players = [player for player in waiting_players
                                       if player.entrance_time!=None and ((time.time()-player.entrance_time) > GlobalConstant.waiting_time_threshold)]
            self.remove_players(waited_too_long_players)
            users_to_end += waited_too_long_players
        if len(users_to_game) > 0: # new game is formed
            self.session.vars["paying_round_"+str(self.game_number)] = self.get_paying_round()
            self.game_number += 1
        self.tot_players_proceed += len(users_to_game) + len(users_to_end)
        return users_to_game+users_to_end if len(users_to_game+users_to_end) > 0 else None

    @staticmethod
    def remove_players(players):
        for player in players:
            player.is_in = False
            # player.beg_active_time is None if the first entrance
            if player.beg_active_time != None and player.is_active:
                player.active_seconds += time.time() - player.beg_active_time
                # fixing other attributes of player, so it will be always consistent
                player.is_active = False
                player.beg_active_time = None
                player.beg_passive_time = time.time()

    @staticmethod
    def set_game(active_players,game_number):
        for player in active_players:
            player.set_game(game_number,len(active_players))
            player.is_in = True

    @staticmethod
    def force_passive(players):
        for player in players:
            player.force_passive = True

    @staticmethod
    def get_paying_round():
        return random.randint(1, GlobalConstant.game_rounds)
        # if random.choice(["1st round", "random_round"]) == "1st round":
        #     return 1
        # else:
        #     return random.randint(1,GlobalConstant.game_rounds)

    @staticmethod
    def sort_by_entrace(player):
        if player.entrance_time == None:
            return -1
        else:
            return player.entrance_time

    # @staticmethod
    # def set_number_of_currently_waiting(players):
    #     sum_active_waiting = sum([player.is_active for player in players])
    #     for player in players:
    #         player.currently_waiting_participants = sum_active_waiting

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    is_active = models.BooleanField(initial=True)  # if the player is active or not
    is_in = models.BooleanField(initial=True)  # if the player can enter a game
    force_passive = models.BooleanField(initial=False) # should we force him to be passive
    force_active = models.BooleanField(initial=True) # should we force him to be active
    entrance_time = models.FloatField(initial=None)
    beg_passive_time = models.FloatField(initial=None) # time he transformed to passive or None if he is active
    beg_active_time = models.FloatField(initial=None) # time he transformed to active or None if he is passive
    active_seconds = models.FloatField(initial=0.0) # total number of seconds he was active till now
    # currently_waiting_participants = models.IntegerField(initial=0)
    email = models.StringField(initial="")

    def set_game(self,game_number,num_participants):
        self.participant.vars["game_number"] = game_number
        self.participant.vars["num_participants_in_game"] = num_participants
        self.participant.vars["number_of_timeouts"] = 0

    def set_status(self):
        if self.force_active:
            # entrance to the wait page - most be active
            self.is_active = True
            self.force_active = False
            self.entrance_time = time.time()
            self.beg_active_time = time.time()
            self.beg_passive_time = None
            return self.is_active
        if self.force_passive:
            if self.is_active:
                self.active_seconds += time.time() - self.beg_active_time
                self.beg_active_time = None
                self.beg_passive_time = time.time()
            self.is_active = False
            self.force_passive = False
            return self.is_active
        if not self.is_active: # was passive and come to get change
            if Constants.passive_allowed_time <= (time.time() - self.beg_passive_time):
                # he was passive more time then allowed -
                # should remain passive, in the next reload he'd be changed to active.
                self.beg_passive_time = time.time()
                return self.is_active # False
        # was passive and now is changing to active
        if not self.is_active:
            self.beg_active_time = time.time()
            self.beg_passive_time = None
        else: # was active and is now changing to passive
            self.active_seconds += time.time() - self.beg_active_time
            self.beg_active_time = None
            self.beg_passive_time = time.time()
        self.is_active = not self.is_active
        return self.is_active

    # after this number of seconds the waitpage would be refreshed
    # the refresh would get the player out of waiting to the end page - according to waiting_time_threshold
    def seconds_left_to_refresh(self):
        return round(Constants.waiting_time_threshold - (time.time()-self.entrance_time)) + 2