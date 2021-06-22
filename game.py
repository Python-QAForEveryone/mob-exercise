def game(user1_input, user2_input):
    user1_input = user1_input.lower()
    user2_input = user2_input.lower()

    if user1_input == user2_input:
        return "Draw"
    elif (user1_input == "rock") and (user2_input == "scissors"):
        return "User1 won!!!"
    elif (user2_input == "rock") and (user1_input == "scissors"):
        return "User2 won!!!"
    elif (user1_input == "rock") and (user2_input == "paper"):
        return "User2 won!!!"
    elif (user2_input == "rock") and (user1_input == "paper"):
        return "User1 won!!!"
    elif (user1_input == "paper") and (user2_input == "scissors"):
        return "User2 won!!!"
    elif (user2_input == "paper") and (user1_input == "scissors"):
        return "User1 won!!!"
    else:
        return "You input a wrong value!!!"

parameter1 = input('Input User1 choose (rock, paper or scissors): ').lower()
parameter2 = input('Input User2 choose (rock, paper or scissors): ').lower()

lst = ['rock', 'paper', 'scissors']

if parameter1 in lst and  parameter2 in lst:
    print(game(parameter1, parameter2))
else:
    print ("Error input")
    if parameter1 not in lst:
        print("Input User1 Error!")
    else:
        print("Input User2 Error!")