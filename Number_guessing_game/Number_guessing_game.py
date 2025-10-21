from math import floor

def guess_number(min_input, max_input):
    min_val = min_input
    max_val = max_input
    attempts = 0

    while True:
        attempts += 1
        middle = floor((min_val + max_val) / 2)

        guess_input = input(f'Is your number.. {middle}? (y)(n): ').lower()
        
        if guess_input == 'y':
            print('YESSS! I guessed it! I win! Thanks for playing!')
            print(f'I guessed the number in: {attempts} tries O _ O')
            break
        elif guess_input == 'n':
            while True:
                newguess_input = input('Higher or lower? (h)/(l): ').lower()
                if newguess_input == 'h':
                    min_val = middle + 1
                    break
                elif newguess_input == 'l':
                    max_val = middle - 1
                    break
                else:
                    print('Enter a valid input.')


def start_game():
    while True:
        start_game = input('Welcome to the number guesser, have you thought of a number yet? (y)/(n): ').lower()
        if start_game == 'n':
            print('keep thinking..')
            continue
        elif start_game == 'y':
            break
        else:
            print('Please enter a valid input.')

def get_range():
    while True:
        try:
            min_input = int(input('Give me a minimum value to go down to: '))
            max_input = int(input('Give me a maximum value to go up to: '))
            if min_input >= max_input:
                print('Minimum number cannot be equal to or greater than the maximum number. Try again.')
                continue
            return min_input, max_input
        except ValueError:
            print('Please enter valid numbers')

def main():

    print('''$$\   $$\                         $$\                                                                                                       
    $$$\  $$ |                        $$ |                                                                                                      
    $$$$\ $$ |$$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\         $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$\  
    $$ $$\$$ |$$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$  __$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|$$  __$$\ $$  __$$\ 
    $$ \$$$$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      $$ /  $$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\  $$$$$$$$ |$$ |  \__|
    $$ |\$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |            $$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\ $$   ____|$$ |      
    $$ | \$$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |            \$$$$$$$ |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |      
    \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|             \____$$ | \______/  \_______|\_______/ \_______/  \_______|\__|      
                                                                          $$\   $$ |                                                            
                                                                         \$$$$$$  |                                                            
                                                                          \______/                                                             ''')

    print('--------------------------------------------------------------------------------------------------------------------------------------------')

    start_game()

    print("Perfect! I'm now going to guess that number.")

    min_input, max_input = get_range()

    guess_number(min_input, max_input)

            
if __name__ == '__main__':
    main()