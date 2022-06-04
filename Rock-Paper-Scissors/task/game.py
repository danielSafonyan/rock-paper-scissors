import random


def read_user_info():
    print("Enter your name: ", end='')
    user_name = input()
    print("Hello,", user_name)
    options = input()
    if not options:
        options = 'Rock, Paper, Scissors'.lower().split(', ')
    else:
        options = options.split(',')
    user_score = 0
    with open('rating.txt') as file:
        for line in file:
            name, score = line.split()
            if name == user_name:
                user_score = score

    print("Okay, let's start")
    return user_name, int(user_score), options


def evaluate_normal_game():
    global user_score
    if who_beats_who[user_choice] == computer_choice:
        print(f"Well done. The computer chose {computer_choice} and failed")
        user_score += 100
    elif who_beats_who[computer_choice] == user_choice:
        print(f"Sorry, but the computer chose {computer_choice}")
    else:
        print(f"There is a draw {computer_choice}")
        user_score += 50


def evaluate_game():
    global user_score
    if options == 'Rock, Paper, Scissors'.lower().split(', '):
        evaluate_normal_game()
    else:
        user_choice_index = options.index(user_choice)
        list_wo_user_choice = options[user_choice_index + 1:] + options[:user_choice_index]
        median = len(list_wo_user_choice) // 2
        user_wins_list = list_wo_user_choice[median:]
        user_loses_list = list_wo_user_choice[:median]

        if computer_choice in user_wins_list:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
        elif computer_choice in user_loses_list:
            print(f"Sorry, but the computer chose {computer_choice}")
        elif computer_choice == user_choice:
            print(f"There is a draw {computer_choice}")
            user_score += 50


# rock beats scissors,
# paper wins over rock,
# scissors defeats paper

who_beats_who = {
    'paper': 'rock',
    'scissors': 'paper',
    'rock': 'scissors'
}


user_name, user_score, options = read_user_info()

while True:
    user_choice = input()
    if user_choice == '!exit':
        print("Bye!")
        break
    if user_choice == '!rating':
        print("Your rating:", user_score)
        continue
    if user_choice not in options:
        print('Invalid input')
        continue

    computer_choice = random.choice(options)
    evaluate_game()




