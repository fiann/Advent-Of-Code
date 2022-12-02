"""
Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide 
(your puzzle input) that they say will be sure to help you win. "The first column 
is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. 
The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, 
Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the 
responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total 
score is the sum of your scores for each round. The score for a single round is the 
score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus 
the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 
6 if you won).

https://adventofcode.com/2022/day/2
"""


def score_for_round(opponent, response):
    score = 0
    if response == "rock":
        score += 1
    elif response == "paper":
        score += 2
    elif response == "scissors":
        score += 3
    if response == opponent:
        score += 3
    if (
        (opponent == "rock" and response == "paper")
        or (opponent == "paper" and response == "scissors")
        or (opponent == "scissors" and response == "rock")
    ):
        score += 6
    return score


# Convert A, B, C to rock, paper, scissors
def decode(value):
    if value == "A" or value == "X":
        return "rock"
    elif value == "B" or value == "Y":
        return "paper"
    elif value == "C" or value == "Z":
        return "scissors"
    raise ValueError(f"Invalid value: {value}")


# Convert X, Y, Z to lose, draw, win
def decode_strategy(value):
    if value == "X":
        return "lose"
    elif value == "Y":
        return "draw"
    elif value == "Z":
        return "win"
    raise ValueError(f"Invalid value: {value}")


# Using the strategy guide, what is your total score?
with open("day-02-input.txt", "r") as file:
    score = 0
    for line in file:
        opponent, response = map(decode, line.rstrip().split())
        score += score_for_round(opponent, response)
    print(f"Naive Score: { score }")

# Calculating strategy
with open("day-02-input.txt", "r") as file:
    score = 0
    for line in file:
        opponent, strategy = line.rstrip().split()
        opponent = decode(opponent)
        strategy = decode_strategy(strategy)
        response = opponent
        if opponent == "rock":
            if strategy == "win":
                response = "paper"
            elif strategy == "lose":
                response = "scissors"
        elif opponent == "paper":
            if strategy == "win":
                response = "scissors"
            elif strategy == "lose":
                response = "rock"
        elif opponent == "scissors":
            if strategy == "win":
                response = "rock"
            elif strategy == "lose":
                response = "paper"
        score += score_for_round(opponent, response)
        print(
            f"Round: { opponent } { strategy } { response } - { score_for_round(opponent, response) }"
        )
    print(f"Strategy Score: { score }")
