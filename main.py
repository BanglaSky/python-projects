x = input('Do you want to take part in a survey?')

if x.lower() == 'yes':
    print('Lets start then')
else:
    quit()

friends = int(input("How many friends do you have?"))

if friends <= 5:
    print('Damn you are lonely')

if friends >= 6:
    print('That is good')
else:
    quit()
rate = int(input('How would you rate them on a scale from 1 - 10?'))

if rate <= 4:
    print('You should get new friends')
elif rate >= 5:
    print('That is great to hear')
else:
    print('Error')
