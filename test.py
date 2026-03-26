import random 

name = input("¿What's your name? ")

if not name:
    name = "Anonymous"


question = input("Ask me something " + name + ": ")


answer = ""

ball = random.randint(1, 9)

if ball == 1:
    answer = "Yes - definitely"
elif ball == 2:
    answer = "It is decidedly so"
elif ball == 3:
    answer = "Without a doubt"
elif ball == 4:
    answer = "Reply hazy, try again"
elif ball == 5:
    answer = "Ask again later"
elif ball == 6:
    answer = "Better not tell you now"
elif ball == 7:
    answer = "My sources say no"
elif ball == 8:
    answer = "Outlook not so good"
elif ball == 9:
    answer = "Very doubtful"

    
if not question:
    print("Do you really don't want to ask?")
else:
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")