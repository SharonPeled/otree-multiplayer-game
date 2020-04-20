from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class FirstWP(WaitPage):
    template_name = 'match/MatchWP.html'
    group_by_arrival_time = True

    def get_players_for_group(self, waiting_players):
        group_size = Constants.group_size
        active_players = [w for w in waiting_players if w.active]
        passive_players = [w for w in waiting_players if not w.active]
        if len(active_players) >= group_size:
            return active_players[:group_size]
        return passive_players



class ActivePage(Page):
    def is_displayed(self) -> bool:
        return self.player.active


class PassivePage(Page):
    def is_displayed(self) -> bool:
        return not self.player.active


page_sequence = [
    FirstWP,
    ActivePage,
    PassivePage,
]
