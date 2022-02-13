print('Welcome to my computer')

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0

answer = input('What does HTML stand for? ')
if answer.lower() == "hyper text markup language":
    print('Correct!You are smart')
    score += 1
else:
    print('Incorrect!')

answer = input('What does CSS stand for? ')
if answer.lower() == "cascading style sheet":
    print('Correct!You are smart')
    score += 1
else:
    print('Incorrect!')

answer = input('What does JS stand for? ')
if answer.lower() == "javascript":
    print('Correct!You are smart')
    score += 1
else:
    print('Incorrect!')

answer = input('What does GPU stand for? ')
if answer.lower() == "graphics processing unit":
    print('Correct!You are smart')
    score += 1
else:
    print('Incorrect!')

answer = input('What does CPU stand for? ')
if answer.lower() == "central processing unit":
    print('Correct!You are smart')
    score += 1
else:
    print('Incorrect!')

print("You have " + str(score) + " questions correct!")
print("----------------------")
print("----------------------")
