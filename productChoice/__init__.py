import itertools
from otree.api import *

doc = """
Product Choice: Online Store A/B Testing (Nudge vs Control)
"""


class C(BaseConstants):
    NAME_IN_URL = "productChoice"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    PRODUCT_NAME = "Stainless Steel Water Bottle (750ml)"
    PRODUCT_PRICE = cu(15)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()
    buy = models.BooleanField(
        label=f"Would you like to buy this product for {C.PRODUCT_PRICE}?",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [True, "Yes, buy now"],
            [False, "No, pass"],
        ],
    )


def creating_session(subsession: Subsession):
    treatments = itertools.cycle(["control", "social_nudge"])
    for player in subsession.get_players():
        player.treatment = next(treatments)


# ===========================================================================
# --- PAGES ---
# ===========================================================================


class Decision(Page):
    form_model = "player"
    form_fields = ["buy"]


class Results(Page):
    pass


page_sequence = [Decision, Results]
