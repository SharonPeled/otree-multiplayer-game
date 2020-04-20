from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class GameWaitPage(WaitPage):
    template_name = 'multiple_groups/GameWaitPage.html'
    group_by_arrival_time = True

    def after_all_players_arrive(self):
        pass


class ActivePage(Page):
    def is_displayed(self) -> bool:
        return self.player.is_player_active and self.player.is_player_in


class PassivePage(Page):
    def is_displayed(self) -> bool:
        return not (self.player.is_player_active and self.player.is_player_in)


class TestPage(Page):
    timeout_seconds = 3
    pass


page_sequence = [GameWaitPage, ActivePage, PassivePage]
