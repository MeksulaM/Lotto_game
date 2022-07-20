import random
import time
import os


def display_name():

    # this function will display game logo and greeting message
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

    # this function will display message that user inputted numbers right
    # and program is ready to go
    print('----------------------------------------------')
    print('There are 49 numbered balls in the draw booth')
    time.sleep(2)
    print('    The drawing machine is ready to draw     ')
    time.sleep(2)
    print('            The draw has started!            ')
    print('----------------------------------------------')
    time.sleep(2)


def clear_console():

    # this function will clear the console window
    os.system('cls')


# creating list of available numbers
available_numbers = list(range(1, 50))


def main():
    while True:
        clear_console()

        # creation of an empty set to store our numbers
        # set because duplicates will not add up
        selected_numbers = set()

        # creation of empty list to store our lucky numbers
        drawn_numbers = []

        # creation of variable to later store hom many numbers we got right
        guessed_numbers_count = 0

        display_name()

        # asking user for numbers
        # user have to input 6 integers, and while loop will work
        # until list of user inputs has less than 6 numbers in it
        while len(selected_numbers) < 6:
            try:
                # letting user know which number he is inputting
                print(f"{len(selected_numbers) + 1}: ", end='')
                user_input = input()

                # user can quit program by typing 'q'
                if user_input == 'q':
                    quit()

                # converting user input to int, so exception can work
                user_input = int(user_input)

                # making sure that user will not input duplicates
                while user_input in selected_numbers:
                    print('Duplicates are not allowed, type other number')
                    print(f'{len(selected_numbers) + 1}: ', end='')
                    user_input = int(input())

                # adding user number to list of inputs
                selected_numbers.add(user_input)

                # making sure user type number in range 1 to 49
                if user_input > 49 or user_input < 1:
                    selected_numbers.remove(user_input)
                    print('Only numbers from 1 to 49 are allowed, type other number')

            # if user will type something other than integer, this message will be displayed
            # and 'try' block will execute again
            except ValueError:
                print('Something went wrong...')
                print('Make sure to type only integers.')
                print("Also, don't use any spaces and characters")

        display_counting_down()

        # drawing lucky numbers using 'random' library
        for i in range(0, 6):

            # we draw number from available numbers
            drawn_number = random.choice(available_numbers)

            # adding drawn number to list of drawn numbers
            drawn_numbers.append(drawn_number)

            # we can't draw same number twice, so drawn number must be removed
            available_numbers.remove(drawn_number)

            # letting user know what number has been drawn
            print(drawn_number)

            # if drawn number is in user numbers list, we have to give user a 1 point
            if drawn_number in selected_numbers:
                guessed_numbers_count += 1
            time.sleep(1)

        # this code displays final score
        print('----------------------------------------------')
        if guessed_numbers_count == 1:
            print(f'You got {guessed_numbers_count} number right')
        elif guessed_numbers_count == 0:
            print("You didn't get any number right")
        else:
            print(f'You got {guessed_numbers_count} numbers right')

        # asking user if he wants to play again
        # if no, the while loop will be stopped
        choice = input('Do you want to try your luck again? (yes/no): ').upper()
        if choice != 'YES':
            break


if __name__ == '__main__':
    main()
