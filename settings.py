from os import environ
from global_utilities.utils import GlobalConstant

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)


SESSION_CONFIGS = [
    {
        'name': 'full_game',
        'display_name': "Heads/Tails Game",
        'num_demo_participants': 100,
        'app_sequence': ["waiting_room","main_game"]
    }
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = "Sharon123"

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'tac4%hv7pd^z5axbj(3i_wlbi*mrx2so@zpge3)bai-vwd-$1l'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
