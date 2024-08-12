#TODO: Create a common function called 'caesar' that takes the 'text', 'shift' and 'direction' as inputs and gives the output directly by calling that function.
#      Also it gets rid of encrypt() and decrypt() functions

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction not in ("encode","decode"):
    print("You have entered wrong value.")
    exit
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))  

def caesar(text, shift, direction):        
    text_list = list(text)
    for i in range(len(text)):
        position = alphabet.index(text_list[i])
        if direction == "encode":
            new_position = (position + shift) % len(alphabet)
        elif direction == 'decode':
            new_position = (position - shift) % len(alphabet)
        text_list[i] = alphabet[new_position]
        plain_text = ''.join(text_list)
    print(f'The {direction}d text is {plain_text}')

caesar(text=text, shift=shift,direction=direction)