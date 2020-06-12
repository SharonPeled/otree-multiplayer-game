


class GlobalConstant():
    game_rounds = 2
    seconds_to_passive = 20
    passive_allowed_time = 40
    group_size = 3
    active_players_per_group = 2 # number of players per group
    tail_rate=0.95 # percentage of participants who chose Tails to get the bonus
    high_pay=0.40
    low_pay=0.20
    q1_reduce_factor = 1/4
    q2_reduce_factor = 3/4
    time_to_response_first_round = 60
    time_to_response = 120
    penalty = -0.1
    basic_payment = 0.1
    completion_code = "COMPLETION_CODE_HEADS_TAILS_7784"





    # def vars_for_template(self):
    #     group_size = self.group.number_of_tails + self.group.number_of_heads
    #     # number of tails to show the participant
    #     proj_tails_size = int((Constants.active_players_per_group/group_size) * self.group.number_of_tails)
    #     if self.group.number_of_tails >= int(group_size * Constants.tail_rate): # bonus was received in the real case
    #         # bonus was not received in the proj case
    #         if not proj_tails_size >= int(Constants.active_players_per_group * Constants.tail_rate):
    #             proj_tails_size = int(Constants.active_players_per_group * Constants.tail_rate)
    #     else: # bonus was not received in the real case
    #         # bonus was received in the proj case
    #         if proj_tails_size >= int(Constants.active_players_per_group * Constants.tail_rate):
    #             proj_tails_size = int(Constants.active_players_per_group * Constants.tail_rate) - 1
    #     return {
    #         'play': self.player.play,
    #         'penalty': -self.player.penalty,
    #         'game_round': self.round_number,
    #         'number_of_tails':proj_tails_size
    #     }