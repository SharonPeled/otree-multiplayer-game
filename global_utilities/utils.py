

class GlobalConstant():
    game_rounds = 2
    seconds_to_passive = 20
    passive_allowed_time = 40 # after that would be a refresh, for internal use
    group_size = 2 # number of links!
    active_players_per_group = 2 # number of players per group
    tail_rate=0.95 # percentage of participants who chose Tails to get the bonus
    high_pay=0.40
    low_pay=0.20
    q1_reduce_factor = 1/4 # question 1 example
    q2_reduce_factor = 3/4 # question 2 example
    time_to_response_first_round = 15 # time to respond in the first game round
    time_to_response = 15 # time to respond in each game round
    penalty = -0.7 # penalty for cases where the participant was too passive or timed out a lot
    basic_payment = 1 # dollar - only for displaying
    waiting_time_threshold = 0.25*60 # seconds, waiting longer than that will get you to the end page
    activeness_waiting_threshold = 0.7 # percetange of time a user needs to be active in the waiting page in order to get full payment
    timeout_submission_rate_threshold = 0.3 # if a user timed-out more than this percentage of the game rounds he gets penalized.
    completion_code = "COMPLETION_CODE_HEADS_TAILS_7784"
