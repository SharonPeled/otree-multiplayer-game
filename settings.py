from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
        name='Nash_T',
        display_name='Nash_T',
        num_demo_participants=3,
        app_sequence=['Nash_T'],
    ),
    dict(
        name='Nash_T_Entrance',
        display_name='Nash_T_Entrance',
        num_demo_participants=3,
        app_sequence=['Nash_T_Entrance'],
    ),
    {
        'name': 'match',
        'display_name': "match",
        'num_demo_participants': 3,
        'app_sequence': ['match'],
    },
    {
        'name': 'my_app',
        'display_name': "my_app",
        'num_demo_participants': 5,
        'app_sequence': ['my_app'],
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'tac4%hv7pd^z5axbj(3i_wlbi*mrx2so@zpge3)bai-vwd-$1l'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
