alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift):
    plain_text_list = list(plain_text)
    
    for i in range (len(plain_text_list)):
        position = alphabet.index(plain_text_list[i])
        new_position = (position + shift)%len(alphabet)
        
        plain_text_list[i] = alphabet[new_position]
        
    cipher_text = ''.join(plain_text_list)
    
    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift):

    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"
    
    cipher_text_list = list(cipher_text)
    
    for i in range(len(cipher_text_list)):
        position = alphabet.index(cipher_text_list[i])
        new_position = (position - shift)%len(alphabet)
        
        cipher_text_list[i] = alphabet[new_position]
    
    plain_text = ''.join(cipher_text_list)
    
    print(f"The decoded text is {plain_text}")    




#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
    encrypt(plain_text=text, shift=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift=shift)