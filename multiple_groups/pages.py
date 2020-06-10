from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


# Page 1: General information about the experiment
class EntrancePage(Page):
    pass


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
        at_least_tails_to_get_bonus = int(Constants.active_players_per_group * Constants.tail_rate)
        get_bonus1 = q1_tail_num >= at_least_tails_to_get_bonus
        get_bonus2 = q2_tail_num >= at_least_tails_to_get_bonus
        return {
            'player_answer1': self.player.in_round(1).q1_answer,
            'player_answer2': self.player.in_round(1).q2_answer,
            'is_player_correct1': self.player.in_round(1).q1_answer == "40" if get_bonus1
            else self.player.in_round(1).q1_answer == "0",
            'is_player_correct2': self.player.in_round(1).q2_answer == "40" if get_bonus1
            else self.player.in_round(1).q2_answer == "0",
            'right_pay1':Constants.high_pay if get_bonus1 else 0,
            'right_pay2':Constants.high_pay if get_bonus2 else 0,
            'q1_tail_num': q1_tail_num,
            'q2_tail_num': q2_tail_num,
        }


# Page 5: Waiting page, waiting for enough active players to form a group
class GameWaitPage(WaitPage):
    template_name = 'multiple_groups/GameWaitPage.html'
    group_by_arrival_time = True

    def after_all_players_arrive(self):
        pass


# Page 6: Main Game - Heads/Tails choice
# class MainGame(Page):
#     form_model = 'player'
#     form_fields = ['play']
#
#     # #timeout_seconds = Constants.time_to_response
#     # def get_timeout_seconds(self):
#     #     if self.round_number < Constants.first_rounds:
#     #         return Constants.time_to_response_first_rounds
#     #     else:
#     #         return Constants.time_to_response
#     #
#     # def before_next_page(self):
#     #    self.player.cond=Constants.t_rate
#     #    if self.timeout_happened:
#     #         self.player.timeout_submission = 1
#     #         self.player.penalty = 0.4
#     #         if random.randint(1, 2) == 1:
#     #             self.player.play_in =True
#     #         else:
#     #             self.player.play_in = False
#     #    else:
#     #         self.player.timeout_submission = 0
#     #         self.player.penalty = 0
#
#     def vars_for_template(self):
#         return {
#             'game_round': self.round_number,
#             'at_least_tails_to_get_bonus': int(Constants.active_players_per_group*Constants.tail_rate)-1,
#             'not_enough_tails_to_get_bonus': int(Constants.active_players_per_group*Constants.tail_rate)-2,
#             'group_size_without_current': Constants.active_players_per_group-1
#         }



class ActivePage(Page):

    def is_displayed(self) -> bool:
        return self.player.is_active and self.player.is_in




class PassivePage(Page):

    def is_displayed(self) -> bool:
        return not self.player.is_active or not self.player.is_in



page_sequence = [GameWaitPage, ActivePage, PassivePage]
# page_sequence = [EntrancePage, Demographic, InitInformation, ExampleQuestions,
#                  ExampleAnswers, GameWaitPage, ActivePage, PassivePage]


