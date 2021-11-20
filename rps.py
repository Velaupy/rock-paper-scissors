import random,os,time

choices = ["rock","paper","scissors"]
choicescounteracts = {
    "rock" : {
        "paper" : False,
        "scissors" : True,
    },
    "paper" : {
        "rock" : True,
        "scissors" : False,
    },
    "scissors" : {
        "rock" : False,
        "paper" : True,
    },
}

os.system("cls")

plrchoice = input("rock paper or scissors??: ").lower()

if not plrchoice in choices:
    print("invalid choice lol")
    time.sleep(1.5)
    exit()

customchoice = random.choice(choices)

print(f"i choose {customchoice}")
print()

playerwins = False
try:
    playerwins = choicescounteracts[plrchoice][customchoice]
except:
    playerwins = "tie"

if playerwins == True:
    print("you win!!!")
elif playerwins == False:
    print("you lose!!!")
elif playerwins == "tie":
    print("tie!!!")
time.sleep(1.5)
exit()