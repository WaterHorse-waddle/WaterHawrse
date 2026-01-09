import random
user_score=0
cmp_score=0
while True:
    choices=["rock", "paper", "scissors"]
    user_choice=input(("Choose among rock, paper or  scissors: ")).lower()
    print(f"You chose: {user_choice}")
    comp_choice=random.choice(choices)
    print(f"Computer chose: {comp_choice}")
    if user_choice not in choices:
        print("Invalid response!")
    elif (user_choice==comp_choice):
        print("Tie")
    elif(user_choice=="rock" and comp_choice=="paper") or (user_choice=="scissors" and comp_choice=="rock") or (user_choice=="paper" and comp_choice=="scissors"):
        print("Computer wins!")
        cmp_score+=1
    else:
        print("You win!")
        user_score+=1
    print(f"Computer Score: {cmp_score}")
    print(f"Player score: {user_score}")