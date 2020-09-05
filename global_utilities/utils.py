

class GlobalConstant():
    game_rounds = 60
    seconds_to_passive = 20
    passive_allowed_time = 40 # after that would be a refresh, for internal use
    group_size = 100 # number of links!
    active_players_per_group = 10 # number of players per group
    tail_rate=0.95 # percentage of participants who chose Tails to get the bonus
    high_pay=0.40
    low_pay=0.20
    q1_reduce_factor = 1/4 # question 1 example
    q2_reduce_factor = 3/4 # question 2 example
    time_to_response_first_round = 10 # time to respond in the first game round
    time_to_response = 10 # time to respond in each game round
    penalty = -0.7 # penalty for cases where the participant was too passive or timed out a lot
    penalty_for_first_phase = -0.8 # the payment for participants in first phase only
    basic_payment = 1 # dollar - only for displaying
    waiting_time_threshold = 15*60 # seconds, waiting longer than that will get you to the end page
    activeness_waiting_threshold = 0.7 # percetange of time a user needs to be active in the waiting page in order to get full payment
    timeout_submission_rate_threshold = 0.3 # if a user timed-out more than this percentage of the game rounds he gets penalized.
    experiment_starting_time = "Sep 3, 2020 08:14:30" # timer for this time - New york Time!!
    reminder_time = 3 # number of minutes before the experiments starts to send a reminder
    sender_email = "otree.dev.experiments@gmail.com" # email to send emails from
    sender_email_password = "OtreeDev2020"
    email_title = "Reminder for upcoming experiment - Head/Tails"
    email_body_sentences = f"""["Dear participant,",
        "",
        "This is a reminder for an upcoming experiment - Heads/Tails.",
        "The experiment starts on {experiment_starting_time} NY time, which is 3 minutes from the time sending this email.",
        "You can now return to your browser tab and complete the experiment.",
        "Completing the experiment will get you the full payment + bonus.",
        "",
        "Happy experimenting and thank you for your collaboration!"
    ]"""
    completion_code = "COMPLETION_CODE_HEADS_TAILS_7784"
