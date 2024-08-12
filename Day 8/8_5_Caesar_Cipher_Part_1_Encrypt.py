alphabet = []

for i in range(ord('a'),ord('z')+1):
    alphabet.append(chr(i))
    
# print(alphabet)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")

text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))

# Todo-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
    # Todo-2: Inside the encrypt function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text
    # e.g.: 
    # plain_text = 'hello'
    # shift = 5
    # cipher_text = 'mjqqt'
    # print output : "The encoded text is mjqqt"

                                # The below commented code is dynamic
                                # text_list = list(text)
                                # for i in range(len(text_list)):
                                #     if text_list[i].isalpha():
                                #         text_list[i] = chr(ord(text_list[i]) + shift)
                                #     else:
                                #         pass #do not do anything
                                    
                                    
                                # cipher_text= ''.join(text_list)
                                
                                # print(f'The encoded text is {cipher_text}')
    
    text_list = list(text)
    
    for i in range (len(text_list)):
        position = alphabet.index(text_list[i])
        new_position = (position + shift)%len(alphabet)
        
        text_list[i] = alphabet[new_position]
        
    cipher_text = ''.join(text_list)
    
    print(f"The encoded text is {cipher_text}") 
        
        

        
    
    
    


# Todo-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text,shift)