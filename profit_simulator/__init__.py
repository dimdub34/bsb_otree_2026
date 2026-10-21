from otree.api import *


doc = """
Profit simulator
"""


class C(BaseConstants):
    NAME_IN_URL = "profit_simulator"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    unit_price = 20
    unit_cost = 5
    fixed_cost = 50


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    quantity = models.IntegerField(label="Quantity", min=0, max=100)


# PAGES
class QuantityInput(Page):
    form_model = Player
    form_fields = ["quantity"]

    @staticmethod
    def js_vars(player: Player):
        return dict(
            unit_price=C.unit_price,
            unit_cost=C.unit_cost,
            fixed_cost=C.fixed_cost,
        )


page_sequence = [QuantityInput]
