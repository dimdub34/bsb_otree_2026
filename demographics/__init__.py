from otree.api import *
import random


doc = """
Demographic Survey
"""


class C(BaseConstants):
    NAME_IN_URL = "demographics"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    is_bot = models.BooleanField(initial=False)
    gender = models.StringField(
        label="What is your gender",
        choices=["Male", "Female", "Other", "Prefer not to say"],
        widget=widgets.RadioSelectHorizontal,
    )
    age = models.IntegerField(label="What is your age", min=18, max=100)
    marital_status = models.StringField(
        label="What is your marital status",
        choices=[
            "Single",
            "Married",
            "Divorced",
            "Widowed",
            "Separated",
            "Prefer not to say",
        ],
        widget=widgets.RadioSelect,
    )
    student = models.BooleanField(
        label="Are you a student?", widget=widgets.RadioSelectHorizontal
    )
    level_of_study = models.StringField(
        label="What is the highest level of education you have completed?",
        choices=[
            "Bachelor's degree",
            "Master's degree",
            "Doctorate or professional degree",
        ],
        widget=widgets.RadioSelect,
    )
    field_of_study = models.StringField(
        label="What is your field of study?",
        choices=[
            "Education",
            "Sciences",
            "Engineering",
            "Law and Political Science",
            "Agriculture and Food",
            "Health",
            "Economics and Management",
            "Technical Studies",
        ],
    )


# PAGES
class Demographics(Page):
    form_model = "player"
    form_fields = [
        "gender",
        "age",
        "marital_status",
        "student",
    ]
    timeout_seconds = 30

    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.is_bot = True
            player.gender = random.choice(
                ["Male", "Female", "Other", "Prefer not to say"]
            )
            player.age = random.randint(18, 100)
            player.marital_status = random.choice(
                [
                    "Single",
                    "Married",
                    "Divorced",
                    "Widowed",
                    "Separated",
                    "Prefer not to say",
                ]
            )
            player.student = random.choice([True, False])


class StudentDetails(Page):
    form_model = "player"
    form_fields = ["level_of_study", "field_of_study"]

    def is_displayed(player: Player):
        return player.student

    def error_message(player: Player, values):
        if (
            values.get("level_of_study") == "Doctorate or professional degree"
            and player.age < 21
        ):
            return "You must be at least 21 years old to pursue a doctorate or professional degree. Please revise your level of study."

    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.level_of_study = random.choice(
                [
                    "Bachelor's degree",
                    "Master's degree",
                    "Doctorate or professional degree",
                ]
            )
            player.field_of_study = random.choice(
                [
                    "Education",
                    "Sciences",
                    "Engineering",
                    "Law and Political Science",
                    "Agriculture and Food",
                    "Health",
                    "Economics and Management",
                    "Technical Studies",
                ]
            )


class Summary(Page):
    def vars_for_template(player: Player):
        profile = f"You declared yourself as a {player.gender}, {player.age} years old, and {player.marital_status}. "
        if player.student:
            profile += f"You are a student in {player.level_of_study} in the field of {player.field_of_study}."
        return dict(profile=profile)


page_sequence = [Demographics, StudentDetails, Summary]
