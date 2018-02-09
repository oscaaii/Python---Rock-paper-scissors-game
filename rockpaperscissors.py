
def main():
    from random import randint
    rpsChoices = ["rock","paper","scissors"]
    rpsP = input("rock, paper, or scissors?: ")
    rpsC = rpsChoices[randint(0,2)]

    print("You chose",rpsP)
    print("The computer chose",rpsC)
    if rpsC == rpsP:
        print("You tied")
    elif rpsC == "paper" and rpsP == "rock" or rpsC == "rock" and rpsP == "scissors" or rpsC == "paper" and rpsP == "rock":
        print("You lose")
    else:
        print("You win")

main()
