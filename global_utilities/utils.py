

class GlobalConstant():
    game_rounds = 60 # number of round in the main_game
    seconds_to_passive = 20 # number of seconds till the player become passive
    passive_allowed_time = 40 # for internal use - after than amount of seconds would be refresh to prevent
    # auto refresh to corrupt the mechanism of passive/active
    group_size = 100 # number of links to the experiment! (be aware the otree doubles the amount of links)
    active_players_per_group = 10 # number of players per group
    tail_rate=0.95 # percentage of participants who chose Tails to get the bonus
    high_pay=0.40 # dollars
    low_pay=0.20 # dollars
    q1_reduce_factor = 1/4 # adjustment for question 1 example
    q2_reduce_factor = 3/4 # adjustment for question 2 example
    time_to_response_first_round = 10 # time to respond in the first game round
    time_to_response = 10 # time to respond in each game round
    penalty = -0.7 # penalty for cases where the participant was too passive or timed out a lot - remeb
    penalty_for_first_phase = -0.8 # the penalty for participants who chose to quit in the first phase (timer phase)
    basic_payment = 1 # dollar, the participation fee - only for displaying, the actual payment is done by MTURK
    waiting_time_threshold = 15*60 # seconds, waiting longer than in waiting_page will get you to the end page
    activeness_waiting_threshold = 0.7 # percetange of time a user needs to be active in the waiting_page in order to get full participation fee
    timeout_submission_rate_threshold = 0.3 # if a user timed-out more than this percentage of game rounds he gets penalized (penalty field).
    experiment_starting_time = "Sep 3, 2020 08:14:30" # New York time - countdown to this time in timer_page for starting the experiment
    reminder_time = 3 # number of minutes before the experiments starts to send a reminder to participantes who asked for it
    sender_email = "otree.dev.experiments@gmail.com" # email to send emails from - make sure that the email's
    # security settings are adjusted correctly - https://pepipost.com/tutorials/how-to-send-emails-with-javascript/
    sender_email_password = "OtreeDev2020" # password to the sender_email
    email_title = "Reminder for upcoming experiment - Head/Tails" # title for the reminder email
    # email message, should be in this format - a string of list of sentences.
    email_body_sentences = f"""["Dear participant,",
        "",
        "This is a reminder for an upcoming experiment - Heads/Tails.",
        "The experiment starts on {experiment_starting_time} NY time, which is 3 minutes from the time sending this email.",
        "You can now return to your browser tab and complete the experiment.",
        "Completing the experiment will get you the full payment + bonus.",
        "",
        "Happy experimenting and thank you for your collaboration!"
    ]"""
    completion_code = "COMPLETION_CODE_HEADS_TAILS_7784" # completion code presented to the participantes
