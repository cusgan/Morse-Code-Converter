# This program is a Finite State Machine 
# that converts a string in Morse Code to Roman alphabet.
# (Handles only letters and not numerals.)

from state_table import state_table

print('\nWELCOME TO MORSE CODE')
print('I will convert your Morse Code to Roman alphabet!')
print('Example: ".... . .-.. .-.. ---" -> "HELLO"\n')

# Prompt user for input
inpt = input('Enter your Morse Code: ')
inpt = inpt.split(' ') # Split the string by Morse code character (each separated by spaceS)

outpt = ''
# Iterate through each 'letter' in Morse Code
for letter in inpt:
    state = 'Start'

    # Iterate through each character that composes a letter
    for char in letter:
        next = None

        # Transitioning from state to state
        # Read the character input
        match (char):
            case '.': next = 0  # Receives dot as input
            case '-': next = 1  # Receives dash as input
            case _:             # Receives invalid input
                state = 'Dead' 
                break
        # Update the state based on the read input
        state = state_table.get(state)[next]

    # Handling invalid inputs
    if (state == 'Start' or state == 'Dead'):
        print('Error: Invalid Morse Code!')
        break

    # Append the resultant Roman letter to the output
    outpt += state.strip()

# Print the final output
print(f'Your Morse Code is: {outpt}\n')