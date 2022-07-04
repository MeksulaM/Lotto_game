import random
import time
import os


def display_name():
    logo = """
    ██╗      ██████╗ ████████╗████████╗ ██████╗ 
    ██║     ██╔═══██╗╚══██╔══╝╚══██╔══╝██╔═══██╗ v.1.0
    ██║     ██║   ██║   ██║      ██║   ██║   ██║
    ██║     ██║   ██║   ██║      ██║   ██║   ██║
    ███████╗╚██████╔╝   ██║      ██║   ╚██████╔╝ 
    ╚══════╝ ╚═════╝    ╚═╝      ╚═╝    ╚═════╝ by Mateusz Meksuła
    """
    print(logo)
    print('----------------------------------------------')
    print('Try your luck and type your six lucky numbers:')
def display_counting_down():
    print('----------------------------------------------')
    print('There are 49 numbered balls in the draw booth')
    time.sleep(2)
    print('    The drawing machine is ready to draw     ')
    time.sleep(2)
    print('            The draw has started!            ')
    print('----------------------------------------------')
    time.sleep(2)
def clear_console():
    os.system('cls')


all_numbers = [i for i in range(1, 50)]

while True:
    clear_console()
    selected_numbers = set()
    drawn_numbers = []
    guessed_numbers_count = 0

    display_name()

    while len(selected_numbers) < 6:
        try:
            print('{}: '.format(len(selected_numbers) + 1), end='')
            x = input()
            if x == 'q':
                quit()
            x = int(x)

            while x in selected_numbers:
                print('Duplicates are not allowed, type other number')
                print('{}: '.format(len(selected_numbers) + 1), end='')
                x = int(input())

            selected_numbers.add(x)

            if x > 49 or x < 1:
                selected_numbers.remove(x)
                print('Only numbers from 1 to 49 are allowed, type other number')

        except Exception:
            print("""Something went wrong... 
Make sure to type only integers. 
Also, don't use any spaces and characters""")

    display_counting_down()

    for i in range(0, 6):
        x = random.choice(all_numbers)
        drawn_numbers.append(x)
        all_numbers.remove(x)
        print(x)
        if x in selected_numbers:
            guessed_numbers_count += 1
        time.sleep(1)

    print('----------------------------------------------')
    if guessed_numbers_count == 1:
        print('You got {} number right'.format(guessed_numbers_count))
    elif guessed_numbers_count == 0:
        print("You didn't get any number right")
    else:
        print('You got {} numbers right'.format(guessed_numbers_count))

    choice = input('Do you want to try your luck again? (yes/no): ').upper()
    if choice != 'YES':
        break
