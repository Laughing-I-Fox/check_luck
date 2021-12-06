import random

list_numbers = []

a = 0


def game():
    global a
    try:
        a = random.randint(int(input('Please enter the first number of range: ')),
                           int(input('Please enter the last number of range: ')))
    except ValueError:
        print('Please enter the correct number!')
        game()
    while True:
        b = int(input('Enter your number: '))
        list_numbers.append(b)
        count = len(list_numbers)
        if b < a:
            print('The number is too small')
        elif b > a:
            print('The number is too large')
        elif b == a and count > 5:
            print('Congratulations! The number is correct!', 'You won in', + count, 'tries!',
                  "But don't buy the lottery today. Today is not your lucky day!")
            break
        elif b == a and count < 5:
            print('Congratulations! The number is correct!', 'You won in', + count, 'tries!',
                  'Today is your lucky day! Buy a lottery!')
            break
    quiz = int(input('If you want to play one more time - enter 1, to exit enter 0: '))
    if quiz == 1:
        game()
    elif quiz == 0:
        print('Thanks for playing, come back and check your luck!')


game()
