#!/usr/bin/env python3

# Course: An Introduction to Interactive Programming in Python (Part 1)
#
# Project: Rock-paper-scissors-lizard-Spock
#
# codeskulptor link:  http://www.codeskulptor.org/#user40_AFNO2Kn6OCwQpIs.py
#
# Use: call "rpsls(name)" to simulate a round of the game (name must be one of:
# "rock", "paper", "scissors", "Spock", "lizard"



import random

#-------------------------------------------------------------------------------
# public section
#-------------------------------------------------------------------------------


# helper functions

#-------------------------------------------------------------------------------

def name_to_number(name):
    name=name.lower()
    assert(name in _game_choices.keys())

    # return _game_choices.keys[name] #one line solution O(1)
    if(name=="rock"):
        result=1
    elif(name=="paper"):
        result=2
    elif(name=="scissors"):
        result=3
    elif(name=="spock"):
        result=4
    elif(name=="lizard"):
        result=5
    return result

#-------------------------------------------------------------------------------

def number_to_name(number):
    assert(int(number))
    assert(number in _rev_game_choices.keys())
    return _rev_game_choices[number] #same result as if elif else 

#-------------------------------------------------------------------------------


def rpsls(player_choice):
    """\param player_choice: "rock", "paper", "scissors", "Spock", "lizard"
    \brief simulates playing a round of Rock-paper-scissors-lizard-Spock.
    """
    
    # print a blank line to separate consecutive games
    print("\n")

    # assert(player_choice.lower() in _game_choices.keys())
    if player_choice.lower() not in _game_choices.keys():
        print("Invalid Player choice! '", player_choice, "', not playing.")
        return 1
    player_choice = player_choice.lower()


    # print out the message for the player's choice
    print("Player chooses ", player_choice)
    
    # convert the player's choice to player_number using the function
    # name_to_number()
    player_choice_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(min(_rev_game_choices.keys()),
                                   max(_rev_game_choices.keys())+1)
    # print("TEST_MSG: comp_number = ", comp_number)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)

    # print out the message for computer's choice
    print("Computer chooses ", comp_choice)

    # compute difference of comp_number and player_number modulo five
    # use if/elif/else to determine winner, print winner message
    game_result = _get_winner(player_choice, comp_choice)
    if game_result==1:
        print("Player wins!")
    elif game_result==2:
        print("Computer wins!")
    else:
        print("Player and computer tie!")

    
#-------------------------------------------------------------------------------

def print_winner_table():
    """Print all the possible (winning) results of the game
    """
    for key, value in _rev_game_choices.items():
        loser1 = (key+2)%5
        if loser1==0:
            loser1=5
        loser2 = (key+4)%5
        if loser2==0:
            loser2=5
        print('{0:2s} wins: {1:3s} {2:4s}'\
        .format(value, _rev_game_choices[loser1], _rev_game_choices[loser2]))


#-------------------------------------------------------------------------------
# private section
#-------------------------------------------------------------------------------

def _get_winner(player1, player2):
    """\param player1, player2: "rock", "paper", "scissors", "spock", "lizard"
    \return 0 = tie; 1 = player1 wins; 2 = player2 wins.
    """
    player1, player2 = player1.lower(), player2.lower()
    assert(player1 in _game_choices.keys())
    assert(player2 in _game_choices.keys())
    return _calculate_winner(_game_choices[player1], _game_choices[player2])

#-------------------------------------------------------------------------------

def _calculate_winner(player1, player2):
    """\param player1, player2: _rev_game_choices keys, thus [1-5] integer.
    \return 0 = tie; 1 = player1 wins; 2 = player2 wins.
    """
    assert(int(player1))
    assert(int(player2))
    assert(player1 in _rev_game_choices.keys())
    assert(player2 in _rev_game_choices.keys())
        
    if(player1==player2):
        return 0

    # import pdb 
    # pdb.set_trace() 
          
    # resolve the modulo arithmetic (warning 5%5 = 0)
    if player2==5:
        player2=0 
    if (player2==(player1+2)%5) or (player2==(player1+4)%5):
        return 1
    else:
        return 2

#-------------------------------------------------------------------------------

# private data area
_game_choices = {"rock":1, "paper":2, "scissors":3, "spock":4, "lizard":5 }
_rev_game_choices = {1:"rock", 2:"paper", 3:"scissors", 4:"spock", 5:"lizard" }

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")
    rpsls("stone") # error test
    print("\n")
