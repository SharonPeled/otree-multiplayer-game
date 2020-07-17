from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

# Page 1: Main Game - Heads/Tails choice
class MainGame(Page):
    form_model = 'player'
    form_fields = ['play']

    def is_displayed(self):
        return self.subsession.round_number != Constants.num_rounds

    def get_timeout_seconds(self):
        if self.round_number == 1: # first round
            return Constants.time_to_response_first_round
        else:
            return Constants.time_to_response

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_submission = 1
            self.player.play = random.choice([True,False])
            self.player.participant.vars["number_of_timeouts"] += 1
        else:
            self.player.timeout_submission = 0

    def vars_for_template(self):
        return {
            'game_round': self.round_number,
            'at_least_tails_to_get_bonus': int(Constants.active_players_per_group*Constants.tail_rate)-1,
            'not_enough_tails_to_get_bonus': int(Constants.active_players_per_group*Constants.tail_rate)-2,
            'group_size_without_current': Constants.active_players_per_group-1
        }


# Page 2: Wait page - for all participants to choose
class ResultsWaitPage(WaitPage):
    group_by_arrival_time = True

    def is_displayed(self) -> bool:
        return self.round_number != 1


#Page 3: Result Page
class ResultsPage(Page):

    def is_displayed(self) -> bool:
        return self.round_number != 1

    def get_timeout_seconds(self):
        if self.round_number == 1: # first round
            return Constants.time_to_response_first_round
        else:
            return Constants.time_to_response

    def vars_for_template(self):
        players = self.group.get_players()
        game_plays = [player.in_round(self.round_number-1).play for player in players
                           if player.participant.vars["game_number"] == self.player.participant.vars["game_number"]]
        number_of_tails = sum(game_plays)
        # if self.player.in_round(self.round_number-1).timeout_submission==1:
        #     payoff = Constants.penalty
        # else:
        if self.player.in_round(self.round_number-1).play == False: # chose head
            payoff = Constants.low_pay
        else: # chose tails
            if number_of_tails >= (int(len(game_plays) * Constants.tail_rate)-1):
                payoff = Constants.high_pay
            else:
                payoff = 0
        return {
            'play': self.player.in_round(self.round_number-1).play,
            'penalty': abs(Constants.penalty) if self.player.in_round(self.round_number-1).timeout_submission==1 else 0,
            'game_round': self.round_number - 1,
            'number_of_tails':number_of_tails,
            'player_payoff': payoff
        }

#Page 6: End Game
class EndGame(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        paying_round = self.session.vars["paying_round_" + str(self.player.participant.vars["game_number"])]
        if self.player.participant.vars["number_of_timeouts"] > Constants.num_rounds*Constants.timeout_submission_rate_threshold:
            final_payoff = Constants.basic_payment + Constants.penalty
            penalized = True
        else:
            final_payoff = self.player.participant.vars["payoff_in_paying_round"]
            penalized = False
            # final_payoff = round(self.player.participant.vars["payoff_in_paying_round"] - Constants.basic_payment,2)
        self.player.payoff = c(final_payoff)
        return {
                'paying_round': paying_round,
                'paying_decision': self.player.participant.vars["play_in_paying_round"],
                'number_entrants': self.player.participant.vars["number_of_tails_in_paying_round"],
                'finalpay': self.player.payoff,
                'paying_round_payoff': round(self.player.participant.vars["payoff_in_paying_round"] - Constants.basic_payment,2),
                'completion_code': Constants.completion_code,
                'is_timeout': penalized,
                'penalty': 0 if not penalized else -Constants.penalty
        }


page_sequence = [ResultsWaitPage, ResultsPage, EndGame, MainGame]
