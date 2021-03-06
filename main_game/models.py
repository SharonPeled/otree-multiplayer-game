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
from collections import Counter
from global_utilities.utils import GlobalConstant

author = 'Sharon Peled'

doc = """
Multi-player game - heads/tails game.
"""


class Constants(BaseConstants):
    name_in_url = 'Heads/Tails_Game'
    players_per_group = None
    num_rounds = GlobalConstant.game_rounds + 1 # special case, final round is only the end page
    group_size = GlobalConstant.group_size
    active_players_per_group = GlobalConstant.active_players_per_group
    tail_rate = GlobalConstant.tail_rate
    high_pay = GlobalConstant.high_pay
    low_pay = GlobalConstant.low_pay
    time_to_response_first_round = GlobalConstant.time_to_response_first_round
    time_to_response = GlobalConstant.time_to_response
    penalty = GlobalConstant.penalty
    completion_code = GlobalConstant.completion_code
    basic_payment = GlobalConstant.basic_payment
    timeout_submission_rate_threshold = GlobalConstant.timeout_submission_rate_threshold


class Subsession(BaseSubsession):

    def group_by_arrival_time_method(self, waiting_players):
        # this function makes sure that the players play within the groups we assigned previously.
        # making sure that each round is played separately for each group.
        c = Counter([player.participant.vars["game_number"] for player in waiting_players])
        users_to_proceed = []
        for player in waiting_players:
            # if all the game participants are waiting
            if c[player.participant.vars["game_number"]] == player.participant.vars["num_participants_in_game"]:
                users_to_proceed.append(player)
        self.set_payoffs(users_to_proceed)
        return users_to_proceed if len(users_to_proceed) > 0 else None

    def set_payoffs(self,users_to_proceed):
        games_numbers = set([player.participant.vars["game_number"] for player in users_to_proceed])
        for game_number in games_numbers:
            game_players = [player for player in users_to_proceed if player.participant.vars["game_number"]==game_number]
            self.set_game_payoffs(game_players,game_number)

    def set_game_payoffs(self,game_players,game_number):
        if not self.session.vars["paying_round_" + str(game_number)] == (
                self.round_number - 1):  # the last round was the paying round
            return
        number_of_tails = sum([player.in_round(self.round_number-1).play for player in game_players])
        for player in game_players:
            player.participant.vars["number_of_tails_in_paying_round"] = number_of_tails
            player.participant.vars["play_in_paying_round"] = player.in_round(self.round_number-1).play
            payoff = 0.0
            # if player.in_round(self.round_number-1).timeout_submission:
            #     payoff += Constants.penalty
            if player.in_round(self.round_number-1).play == False:  # chose heads
                payoff += Constants.low_pay
            else:  # chose tails
                if number_of_tails >= (int(len(game_players) * Constants.tail_rate)-1):
                    payoff += Constants.high_pay
                else:
                    payoff += 0
            player.participant.vars["payoff_in_paying_round"] = round(payoff,2)




class Group(BaseGroup):
    pass


class Player(BasePlayer):
    play = models.BooleanField(choices=[[True,"Tails"], [False, "Heads"]])
    timeout_submission = models.BooleanField(initial=0)
