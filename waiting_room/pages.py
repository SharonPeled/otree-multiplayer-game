from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

# Page 1: Waiting page, waiting for enough active players to form a group
class GameWaitPage(WaitPage):
    template_name = 'waiting_room/GameWaitPage.html'
    group_by_arrival_time = True

    def after_all_players_arrive(self):
        pass

    # def vars_for_template(self):
    #     return {"currently_waiting_participants":self.player.currently_waiting_participants}


# Page 2: Entering the actual game
class ActivePage(Page):
    timeout_seconds = 3

    def is_displayed(self) -> bool:
        return self.player.is_active and self.player.is_in


# Page 2: Game over
class PassivePage(Page):
    form_model = 'player'
    form_fields = ['email']

    def is_displayed(self) -> bool:
        return not self.player.is_active or not self.player.is_in

    def vars_for_template(self) -> dict:
        if self.player.active_seconds > Constants.waiting_time_threshold * Constants.activeness_waiting_threshold:
            # was active enough time to get good payment
            self.player.payoff = c(0.0) # All participation fee
            was_active_enough = True
        else:
            # wan't active very often
            self.player.payoff = c(0.0 + Constants.penalty) # only part of the participation fee
            was_active_enough = False
        return \
        {
            "completion_code":Constants.completion_code,
            "finalpay": self.player.payoff + Constants.basic_payment,
            "was_active_enough": was_active_enough
        }


page_sequence = [GameWaitPage, ActivePage, PassivePage]
