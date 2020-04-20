from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import json


#Page 2: Basic Demographic Information
class Demographic(Page):
    #timeout_seconds = 300

    #def is_displayed(self):
    #    return self.round_number == 1
    pass

page_sequence = [
    Demographic,
]
