####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'hee hee' # Only 10 chars displayed.
strategy_name = 'Betray very often, collude occasionally'
strategy_description = 'There is a small chance the program colludes on its own, otherwise it will betray. Also betrays if the other person betrays.'
    
import random
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''

    if 'c' in their_history[-10:]: # If the other player has betrayed within last 10 rounds, 
        return 'b'               # Betray.
    else:
        if random.random()<0.4: # 10% of the other rounds
            return 'c'         # collude
        else:
            return 'b'         # but 90% of the time betray

