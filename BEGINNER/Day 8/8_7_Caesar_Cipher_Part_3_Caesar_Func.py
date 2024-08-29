#TODO: Create a common function called 'caesar' that takes the 'text', 'shift' and 'direction' as inputs and gives the output directly by calling that function.
#      Also it gets rid of encrypt() and decrypt() functions
import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(text, shift, direction):        
    text_list = list(text)
    
    # TODO: What if the entered text contains the number or special characters?
    # Ans: To ena mate aapne niche if text[i] in alphabet vali condition add kari chhe
    
    for i in range(len(text)):
        if text[i] in alphabet:
            position = alphabet.index(text_list[i])
            if direction == "encode":
                new_position = (position + shift) % len(alphabet)
            elif direction == 'decode':
                new_position = (position - shift) % len(alphabet)
            text_list[i] = alphabet[new_position]
            plain_text = ''.join(text_list)
        elif text[i] not in alphabet:
            plain_text = ''.join(text_list)
    print(f'The {direction}d text is {plain_text}')



# TODO: Ask the user to ask if they want to restart the cipher program?
# Type 'YES' if you want to go again else 'NO'



def yes_or_no():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction not in ("encode","decode"):
        print("You have entered wrong value.")
        sys.exit()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))  


    caesar(text=text, shift=shift,direction=direction)

    y_or_n = input("Type 'yes' if you want to go again. Otherwise type 'no'.: ") 
    if y_or_n == 'yes':
        yes_or_no()
        
        
yes_or_no()