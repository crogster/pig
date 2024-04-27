import random

def roll():
    roll = random.randint(1,6)
    return roll

print('Welcome to PIG. In this interactive game, you will be presented with a standard D6, which can be rolled indefinitely where its value represents and addition to your score! However, if you roll a 1, your score will be ommited and your turn will be over.')
while True:
    try:
        max_Score = (input('What should the score goal be?: '))
        if max_Score.isdigit():
            max_Score = int(max_Score)
    except ValueError:
        print('Please type a valid number.')
    if int(max_Score) <= 0 or type(max_Score) != int:
        print('Please type a valid number.')
    else:
        break

while True:
    player_count = input('Please input the number of players (2-4): ')
    if player_count.isdigit():
        player_count = int(player_count)
        if 2 <= player_count <= 4:
            break
        else:
            print('Please provide a valid amount of players.')
    else:
        print('Please try again.')

player_Scores = [0 for _ in range(player_count)]

while max(player_Scores) < max_Score:

    for player_index in range(player_count):
        print(f"It is player {player_index + 1}'s turn")
        print(f"Your current score is {player_Scores[player_index]}")
        current_score = 0

        while True:
            roll_yes = input('Do you want to roll (y)?: ').lower()
            if roll_yes != 'y':
                break
    
            roll_value = roll()
            if roll_value == 1:
                print('You have rolled a 1, and your score has been reset to 0')
                current_score = 0
                break

            else:
                print(f'You have rolled a {roll_value}')
                current_score += roll_value
            
            print(f'Your score is: {current_score}')

        player_Scores[player_index] += current_score
        print(f'Your total score is {player_Scores[player_index]}')
        
max_player_score = max(player_Scores)
champion_index = player_Scores.index(max_player_score)
print(f'Player {champion_index + 1} has won the game, with a score of {max_player_score}')