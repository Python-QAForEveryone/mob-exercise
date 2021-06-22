def game(parameter1, parameter2):
    if parameter1 == parameter2:
        return "Draw"
    elif (parameter1 == "Rock") and (parameter2 == "Scissors"):
        return "User1 won!!!"
    elif (parameter2 == "Rock") and (parameter1 == "Scissors"):
        return "User2 won!!!"
    elif (parameter1 == "Rock") and (parameter2 == "Paper"):
        return "User2 won!!!"
    elif (parameter2 == "Rock") and (parameter1 == "Paper"):
        return "User1 won!!!"
    elif (parameter1 == "Paper") and (parameter2 == "Scissors"):
        return "User2 won!!!"
    elif (parameter2 == "Paper") and (parameter1 == "Scissors"):
        return "User1 won!!!"
    else:
        return "You input a wrong value!!!"

parameter1 = input('Input User1 choose (Rock, Paper or Scissors): ')
parameter2 = input('Input User2 choose (Rock, Paper or Scissors): ')

lst = ['Rock', 'Paper', 'Scissors']
if lst.__contains__(parameter1) and lst.__contains__(parameter2):
    print(game(parameter1, parameter2))