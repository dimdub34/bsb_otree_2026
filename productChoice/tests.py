import random
from otree.api import Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        # Nudge effect: 80% buy rate with social nudge vs 40% in control
        if self.player.treatment == "social_nudge":
            will_buy = random.random() < 0.8
        else:
            will_buy = random.random() < 0.4

        yield Decision, dict(buy=will_buy)
        yield Results
