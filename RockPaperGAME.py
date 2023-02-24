import random
def game():
    user_choice = input("Enter your choice: 'r' for Rock 's' for sicorrs 'p' for paper:\n")
    computer_choice = random.choice( ["r","s","p"])
    if user_choice==computer_choice:
        return f"game is Tie!!"
    elif user_win(user_choice,computer_choice):
        return f"user win!!"
    return f"comp winn!"
def user_win(user,comp):
    if (user == "r" and comp == "s") or (user == "s" and comp=="p") or (user == "p" and comp=="r"):
        return True

print(game())