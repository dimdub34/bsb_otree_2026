from os import environ

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")
SECRET_KEY = "9487829551031"
DEMO_PAGE_INTRO_HTML = """ """

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

LANGUAGE_CODE = "en"
REAL_WORLD_CURRENCY_CODE = "USD"
USE_POINTS = False

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
)

ROOMS = [
    dict(
        name="my_lab", display_name="My Lab", participant_label_file="_rooms/my_lab.txt"
    ),
]

SESSION_CONFIGS = [
    dict(
        name="english_auction",
        display_name="English Auction",
        app_sequence=["english_auction"],
        num_demo_participants=3,
    ),
    dict(
        name="profit_simulator",
        display_name="Profit Simulator",
        app_sequence=["profit_simulator"],
        num_demo_participants=4,
    ),
    dict(
        name="beauty_contest",
        display_name="Beauty Contest",
        app_sequence=["beauty_contest", "demographics"],
        num_demo_participants=4,
    ),
    dict(
        name="my_first_app",
        display_name="My First Application",
        app_sequence=["my_first_app"],
        num_demo_participants=3,
    ),
    dict(
        name="demographics",
        display_name="Demographic Survey",
        app_sequence=["demographics"],
        num_demo_participants=5,
    ),
    dict(
        name="product_choice",
        display_name="Product Choice - Treatment assigment example",
        app_sequence=["productChoice", "demographics"],
        num_demo_participants=10,
    ),
]
