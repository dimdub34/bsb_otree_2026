from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = "my_first_app"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(label="What is your name?")
    age = models.IntegerField(label="How old are you?")


# PAGES
class Questionnaire(Page):
    form_model = "player"
    form_fields = ["name", "age"]


page_sequence = [Questionnaire]
