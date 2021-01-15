# Social Science Survey

print('Social Science Survey')
print('Instructions: Type in all answers carefully. Do not hit the space bar before typing answers. Answers are not case sensitive.')

print()

myFirearms = None
while myFirearms is None:
    input_value = input('How many firearms do you own? Do not put commas or decimal points.')
    try:
        myFirearms = int(input_value)
    except ValueError:
        print("{input} is not a number, please enter a number only".format(input=input_value))
        continue
if myFirearms > 0:
    print('You own ' + str(int(myFirearms)) + ' firearm/firearms right now.')

print()

while True:
    Use = input('Would you use your firearm in self-defense?')
    if Use.lower() not in ('yes', 'no'):
        print('Not yes or no. Try again.')
    else:
        break
if Use == 'yes':
    print('You answered yes.')
elif Use == 'no':
    print('You answered no.')

print()

while True:
    Gender = input('What is your gender identification? Male, Female, Nonbinary, Other?')
    if Gender.lower() not in ('male', 'female', 'nonbinary', 'other'):
        print('Not one of the listed answer choices. Try again.')
    else:
        break
if Gender == 'male':
    print('You answered Male.')
elif Gender == 'female':
    print('You answered Female.')
elif Gender == 'nonbinary':
    print('You answered Non-Binary.')
elif Gender == 'other':
    print('You answered Other.')

print()

while True:
    Reason = input('Please select the first reason you can think of for why you decided to purchase a firearm:(1) defense, (2) constitution, or (3) sport.')
    if Reason.lower() not in ('defense', 'constitution', 'sport'):
        print('Incorrect answer choice. Try again.')
    else:
            break
if Reason == 'defense':
    print('You chose Defense.')
elif Reason == 'constitution':
    print('You chose Constitution.')
elif Reason == 'sport':
    print('You chose Sport.')

print()

while True:
    myOption = input('Which one of the selected options (numbers 1, 2, and 3) for the previous question is most important to you?')
    if myOption.lower() not in ('1', '2', '3'):
        print("Not an appropriate choice.")
    else:
        break
if myOption == '1':
    print('You answered Defense.')
elif myOption == '2':
    print('You answered 2nd_Amendment_Right.')
elif myOption == '3':
    print('You answered Sport.')

print()

while True:
    Presence = input('How would you rate the amount of police presence in your neighborhood on a scale of 1-10, 10 being high?')
    if Presence.lower() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        print('ONLY select a value from 1 to 10.')
    else:
        break 
print('Your selection is ' + str(int(Presence)))

print()

while True:
    Threatened = input('Do you feel threatened by racially motivated hate groups in the U.S.?')
    if Threatened.lower() not in ('yes', 'no'):
        print('Not yes or no. Try again.')
    else:
        break
if Threatened == 'yes':
    print('You chose yes.')
elif Threatened == 'no':
    print('You chose no.')

print()

while True:
    Scared = input('Do you feel scared of the police in the U.S.?')
    if Scared.lower() not in ('yes', 'no'):
        print('Not yes or no. Try again.')
    else:
        break
if Scared == 'yes':
    print('You chose Yes.')
elif Scared == 'no':
    print('You chose No.')

print()

while True:
    Victimized = input('Have you ever been victimized by police or racially motivated offenders in the U.S.?')
    if Victimized.lower() not in ('yes', 'no'):
        print('Not yes or no. Try again.')
    else:
        break
if Victimized == 'yes':
    print('You chose yes.')
elif Victimized == 'no':
    print('You chose no.')

print()

print('You have completed all of the questions. Thank you for taking this survey.')
