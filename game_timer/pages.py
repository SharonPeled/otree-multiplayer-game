from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Timer_Page(Page):
    form_model = 'player'
    form_fields = ['email', "is_player_wants_to_proceed", "is_player_wants_reminder"]

    def vars_for_template(self) -> dict:
        return \
        {
            "finalpay": c(0.0 + Constants.penalty_for_first_phase) + Constants.basic_payment, # only part of the participation fee
            "experiment_starting_time": Constants.experiment_starting_time,
            "reminder_time": Constants.reminder_time
        }


class QuitPage(Page):
    def is_displayed(self) -> bool:
        return not self.player.is_player_wants_to_proceed

    def vars_for_template(self) -> dict:
        self.player.payoff = c(0.0 + Constants.penalty_for_first_phase) # only part of the participation fee
        return \
        {
            "finalpay": self.player.payoff + Constants.basic_payment,
            "completion_code": Constants.completion_code
        }


class ReminderPage(Page):
    form_model = 'player'
    form_fields = ["is_player_wants_to_proceed"]

    def is_displayed(self) -> bool:
        return self.player.is_player_wants_reminder

    def vars_for_template(self) -> dict:
        return \
        {
            "finalpay": c(0.0 + Constants.penalty_for_first_phase) + Constants.basic_payment, # only part of the participation fee
            "experiment_starting_time": Constants.experiment_starting_time,
            "email": self.player.email,
            "reminder_time": Constants.reminder_time,
            "sender_email": Constants.sender_email,
            "sender_email_password": Constants.sender_email_password,
            "email_title": Constants.email_title,
            "email_body_sentences": Constants.email_body_sentences
        }


page_sequence = [Timer_Page, ReminderPage, QuitPage]
