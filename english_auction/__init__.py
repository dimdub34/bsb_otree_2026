from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = "english_auction"
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1

    BUDGET = 80
    ITEM_VALUE = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    highest_bid = models.IntegerField(initial=10, doc="Highest bid value")
    highest_bidder = models.IntegerField(initial=0, doc="id of player with highest bid")


class Player(BasePlayer):
    bid_amount = models.IntegerField(min=0, max=100)


# PAGES
class Auction(Page):
    timeout_seconds = 60

    @staticmethod
    def live_method(player: Player, data):
        print("Received live data:", data)
        try:
            bid = int(data.get("bid"))
        except (ValueError, TypeError):
            return {
                player.id_in_group: {
                    "error": "Please enter a valid number.",
                    "highest_bid": player.group.highest_bid,
                    "highest_bidder": player.group.highest_bidder,
                }
            }

        if bid > player.group.highest_bid and bid <= C.BUDGET:
            player.group.highest_bid = bid
            player.group.highest_bidder = player.id_in_group
            return {
                0: {
                    "highest_bid": player.group.highest_bid,
                    "highest_bidder": player.group.highest_bidder,
                }
            }
        else:
            return {
                player.id_in_group: {
                    "error": f"Invalid bid. It must be strictly higher than {player.group.highest_bid} and at most {C.BUDGET}.",
                    "highest_bid": player.group.highest_bid,
                    "highest_bidder": player.group.highest_bidder,
                }
            }

    @staticmethod
    def js_vars(player: Player):
        return {"budget": C.BUDGET}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.id_in_group == player.group.highest_bidder:
            player.payoff = C.BUDGET - player.group.highest_bid + C.ITEM_VALUE
        else:
            player.payoff = C.BUDGET


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        is_winner = player.id_in_group == player.group.highest_bidder
        return {
            "is_winner": is_winner,
            "winning_bid": player.group.highest_bid,
            "winner_id": player.group.highest_bidder,
        }


page_sequence = [Auction, Results]
