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
        'num_demo_participants': GlobalConstant.group_size,
        'app_sequence': ['prior_game', "waiting_room", "main_game"],
        'mturk_hit_settings': dict(
            keywords='bonus, study',
            title="Multiplayer Heads/Tails Game",
            description='Academic experiment in which you need to play a very short and simple multi-person game.',
            frame_height=500,
            template='global/mturk_template.html',
            minutes_allotted_per_assignment=300,
            expiration_hours=7 * 24,
            qualification_requirements=[]
            # grant_qualification_id='YOUR_QUALIFICATION_ID_HERE', # to prevent retakes
        )
    },
    {
        'name': 'Nash_T',
        'display_name': "Nash_T",
        'num_demo_participants': 3,
        'app_sequence': ['Nash_T'],
    },
    {
        'name': 'Nash_T_Entrance',
        'display_name': "Nash_T_Entrance",
        'num_demo_participants': 20,
        'app_sequence': ['Nash_T_Entrance'],
    },
    {
        'name': 'single_group',
        'display_name': "single_group",
        'num_demo_participants': 5,
        'app_sequence': ['single_group'],
    },
    {
        'name': 'multiple_groups',
        'display_name': "multiple_groups",
        'num_demo_participants': 20,
        'app_sequence': ['multiple_groups'],
        'mturk_hit_settings': dict(
                                    keywords='bonus, study',
                                    title='multiple_groups',
                                    description='Description for your experiment',
                                    frame_height=500,
                                    template='global/mturk_template.html',
                                    minutes_allotted_per_assignment=60,
                                    expiration_hours=7 * 24,
                                    qualification_requirements=[]
                                    # grant_qualification_id='YOUR_QUALIFICATION_ID_HERE', # to prevent retakes
                                )
    },
    {
        'name': 'waiting_room',
        'display_name': "waiting_room",
        'num_demo_participants': 20,
        'app_sequence': ['waiting_room']
    },
    {
        'name': 'main_game',
        'display_name': "main_game",
        'num_demo_participants': GlobalConstant.group_size,
        'app_sequence': ['waiting_room', 'main_game']
    },
    {
        'name': 'prior_game',
        'display_name': "prior_game",
        'num_demo_participants': 3,
        'app_sequence': ['prior_game']
    }
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
