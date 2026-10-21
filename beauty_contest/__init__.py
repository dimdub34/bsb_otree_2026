from otree.api import *
import random


doc = """
Beauty Contest Game
"""


class C(BaseConstants):
    NAME_IN_URL = "beauty_contest"
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1

    COEFFICIENT = 2 / 3


class Subsession(BaseSubsession):
    pass


def creation_session(subsession: Subsession):
    subsession.group_randomly()


class Group(BaseGroup):
    average = models.FloatField()
    target = models.FloatField()

    def compute_target(self):
        self.average = sum([p.decision for p in self.get_players()]) / len(
            self.get_players()
        )
        # values =  []
        # for p in self.get_players():
        #     values.append(p.decision)
        # self.average = sum(values) / len(values)

        self.target = self.average * C.COEFFICIENT

    def set_winners(self):
        """Return a list of players who chose the number closest to the target."""
        players = self.get_players()
        # compute absolute difference from target for each player
        diffs = {p: abs(p.decision - self.target) for p in players}

        # abs_diffs = {}
        # for p in self.get_players():
        #     abs_diffs[p] = abs(p.decision - self.target)

        # find the minimum difference
        min_diff = min(diffs.values())
        # return all players with that minimum difference
        winners = [p for p, d in diffs.items() if d == min_diff]
        for p in players:
            p.diff_from_target = diffs[p]
            p.is_winner = p in winners


class Player(BasePlayer):
    decision = models.IntegerField(min=0, max=100)
    diff_from_target = models.FloatField()
    is_winner = models.BooleanField(initial=False)


# PAGES
class Decision(Page):
    form_model = Player
    form_fields = ["decision"]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.decision = random.randint(0, 100)


class DecisionWaitForGroup(WaitPage):
    wait_for_all_groups = False

    def after_all_players_arrive(group: Group):
        group.compute_target()
        group.set_winners()


class Results(Page):
    def vars_for_template(player: Player):
        return {
            "average": player.group.average,
            "target": player.group.target,
            "diff": player.diff_from_target,
            "is_winner": player.is_winner,
        }


page_sequence = [Decision, DecisionWaitForGroup, Results]
