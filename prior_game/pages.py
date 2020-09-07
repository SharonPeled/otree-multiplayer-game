from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


# Page 1: General information about the experiment
class EntrancePage(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'basic_payment': c(Constants.basic_payment),
            'high_pay': c(Constants.high_pay),
            'low_pay': c(Constants.low_pay)
        }


# Page 2: Basic demographic form
class Demographic(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']
    timeout_seconds = 300

    def is_displayed(self):
        return self.round_number == 1


# Page 3: Game instructions
class InitInformation(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'at_least_tails_to_get_bonus': int(Constants.active_players_per_group*Constants.tail_rate)-1,
            'not_enough_tails_to_get_bonus': int(Constants.active_players_per_group*Constants.tail_rate)-2,
            'group_size': Constants.active_players_per_group,
            'group_size_without_current': Constants.active_players_per_group-1
        }


# Page 4: Questions to check understanding
class ExampleQuestions(Page):
    form_model = 'player'
    form_fields = ['q1_answer','q2_answer']

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'q1_tail_num': int(Constants.active_players_per_group*Constants.q1_reduce_factor),
            'q2_tail_num': int(Constants.active_players_per_group*Constants.q2_reduce_factor),
        }


# Page 4: Questions Feedback
class ExampleAnswers(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        q1_tail_num = int(Constants.active_players_per_group * Constants.q1_reduce_factor)
        q2_tail_num = int(Constants.active_players_per_group * Constants.q2_reduce_factor)
        at_least_tails_to_get_bonus = int(Constants.active_players_per_group * Constants.tail_rate) -1
        get_bonus1 = q1_tail_num >= at_least_tails_to_get_bonus
        get_bonus2 = q2_tail_num >= at_least_tails_to_get_bonus
        return {
            'player_answer1': self.player.in_round(1).q1_answer,
            'player_answer2': self.player.in_round(1).q2_answer,
            'is_player_correct1': self.player.in_round(1).q1_answer == "40" if get_bonus1
            else self.player.in_round(1).q1_answer == "0",
            'is_player_correct2': self.player.in_round(1).q2_answer == "40" if get_bonus1
            else self.player.in_round(1).q2_answer == "0",
            'right_pay1':"40" if get_bonus1 else 0,
            'right_pay2':"40" if get_bonus2 else 0,
            'q1_tail_num': q1_tail_num,
            'q2_tail_num': q2_tail_num,
        }


page_sequence = [EntrancePage, Demographic, InitInformation, ExampleQuestions,
                 ExampleAnswers]