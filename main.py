#Braden Leach
#December 10 2024
#While loop Practice


import time 
#----While Practice----#
#7-3
active = True 
while active:
    user_inp =input(f'Enter a pizza topping (type quit to exit):\n')
    if user_inp == 'quit':
        break
    else: 
        print(f'\nI really like {user_inp} on my pizza!')

#7-5
active = True 
while active:
    user_age = int(input('What is your age: '))
    if user_age < 3:
        print('The cost for the movies for you would be free!')
        break
    elif user_age < 13:
        print('The cost for the movies for you would be $10!')
        break
    elif user_age > 12:
        print('The cost for the movies for you would be $15!')
        break
    else:
        print('invalid input')

#7-6
counter = 0
active = True 
while active:
    user_inp =input(f'Enter a pizza topping (type quit to exit):\n')
    if user_inp == 'quit':
        active = False
    else: 
        print(f'\nI really like {user_inp} on my pizza!')
        counter += 1
    if counter == 3:
        print('Maximum toppings, getting your pizza ready...')
        time.sleep(2)

        print('\nyour pizza is done!')
        break



