####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E1'
strategy_name = 'Collude occasionally.'
strategy_description = 'Always betray, collude once every 4 rounds.'
    
def move(my_history, their_history, my_score, their_score):
    '''Betray 4 times and the collude the fifth time
    '''
    loop = 0 
    if loop <= 4: #colludes 4 times in a row, return 'c'
      return 'c'
      loop += 1
    return 'b'#betrays for the 4th time , return 'b'