from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import json

##First grouping page.
class MyWaitPage(WaitPage):
    group_by_arrival_time = True

    #def is_displayed(self):
    #    return self.round_number == 1

#Page 1: Basic Demographic Information
class Demographic(Page):
    form_model = 'player'
    form_fields = ['age',
                   'gender']

    timeout_seconds = 300

    def is_displayed(self):
        return self.round_number == 1


#Page 1: Game Instructions
class InitInformation(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'additional_entr': int((Constants.players_per_group*Constants.t_rate)-1),
            'additional_entr2': int((Constants.players_per_group*Constants.t_rate)-2),
            'total_part': int(Constants.players_per_group - 1),
        }
#Page 2: Question
class UnderstandQuestion(Page):
    form_model = 'player'
    form_fields = ['und_quest1','und_quest2']

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'entrants1': int((Constants.players_per_group)*1/4),
            'entrants2': int((Constants.players_per_group)*3/4),
        }
#Page 3: Question Feedback
class UnderstandAnswer(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):

        if int(Constants.players_per_group*1/4) >= int(Constants.players_per_group * Constants.t_rate):  # Enter 40 cents
            pay1=40
            if self.player.in_round(1).und_quest1 == "40":
                cor1 = True
            else:
                cor1 = False
        else:
            pay1=0
            if self.player.in_round(1).und_quest1 == "0":
                cor1 = True
            else:
                cor1 = False

        if int(Constants.players_per_group*3/4) >= int(Constants.players_per_group * Constants.t_rate):  # Enter 40 cents
            pay2=40
            if self.player.in_round(1).und_quest2 == "40":
                cor2 = True
            else:
                cor2 = False
        else:
            pay2=0
            if self.player.in_round(1).und_quest2 == "0":
                cor2 = True
            else:
                cor2 = False

        #if self.player.in_round(1).und_quest1 == "0":
        #    cor1 = True
        #else:
        #    cor1 = False

        #if self.player.in_round(1).und_quest2 == "0":
        #    cor2 = True
        #else:
        #    cor2 = False

        return {
            'answer1': self.player.in_round(1).und_quest1,
            'answer2': self.player.in_round(1).und_quest2,
            'correct1': cor1,
            'correct2': cor2,
            'right_pay1':pay1,
            'right_pay2':pay2,
            'entrants1': int((Constants.players_per_group) * 1 / 4),
            'entrants2': int((Constants.players_per_group) * 3 / 4),
        }


#Page 4: Main Game - Choice
class MainGame(Page):
    form_model = 'player'
    form_fields = ['play_in']


    #timeout_seconds = Constants.time_to_response
    def get_timeout_seconds(self):
        if self.round_number < Constants.first_rounds:
            return Constants.time_to_response_first_rounds
        else:
            return Constants.time_to_response

    def before_next_page(self):
       self.player.cond=Constants.t_rate
       if self.timeout_happened:
            self.player.timeout_submission = 1
            self.player.penalty = 0.4
            if random.randint(1, 2) == 1:
                self.player.play_in =True
            else:
                self.player.play_in = False
       else:
            self.player.timeout_submission = 0
            self.player.penalty = 0

    def vars_for_template(self):
        game_round = self.round_number
        return {
            'game_round': game_round,
            'additional_entr': int((Constants.players_per_group * Constants.t_rate) - 1),
            'additional_entr2': int((Constants.players_per_group * Constants.t_rate) - 2),
            'total_part': int(Constants.players_per_group - 1),
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


#Page 5: Result Page
class Results(Page):

    #timeout_seconds = 300
    #timeout_seconds = Constants.time_to_response

    def get_timeout_seconds(self):
        if self.round_number < Constants.first_rounds:
            return Constants.time_to_response_first_rounds
        else:
            return Constants.time_to_response

    def vars_for_template(self):
            return {
                'my_decision': self.player.play_in,
                'penalty_submission': self.player.penalty,
                'game_round': self.round_number,
            }

#Page 6: End Game
class EndGame(Page):

    timeout_seconds = Constants.time_to_response
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):

        #bonus=self.player.in_round(self.session.vars['paying_round']).outcome+100
        #payoff1=Constants.show_up_fee + self.player.in_round(self.session.vars['paying_round']).outcome + Constants.endowment
        #trial_pay=self.player.in_round(self.session.vars['paying_round']).outcome
        #self.player.payoff=payoff1/Constants.payratio
        #pay_dollar=payoff1/Constants.payratio
        if self.player.in_round(self.session.vars['paying_round']).play_in:
            pd = "TAILS"
        else:
            pd = "HEADS"

        return {
                'paying_round': self.session.vars['paying_round'],
                'paying_decision': pd,
                'number_entrants': self.group.in_round(self.session.vars['paying_round']).number_entrants,
                'finalpay': self.player.in_round(self.session.vars['paying_round']).payoff,
        }


page_sequence = [
    MyWaitPage,
    Demographic,
    #InitInformation,
    #MyWaitPage,
    InitInformation,
    UnderstandQuestion,
    UnderstandAnswer,
    MainGame,
    ResultsWaitPage,
    Results,
    EndGame,
]
