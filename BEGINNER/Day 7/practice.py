import random
word_list = ['abhishek','hetal','bhavik','maitri','amit','krishna','ami','umang','vaibhavi','kalyani','madhavi','nilesh','chetan','chirag','paras','tushar','vishal','nikit','anjali','drashti','parth','kuki','abhay','tirth','dhimant','jaymit','devangi','krupali']

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''




chosen_word = random.choice(word_list)

print(logo)





life = 6
already_guessed = set()

print(chosen_word)

chosen_word_list = list(chosen_word)

guessing_word = '_'*len(chosen_word)
guessing_word_list = list(guessing_word)

while life >0:
    # we will ask the user to guess a letter
    input_letter = input("Guess a letter: ").lower()
    
    # If user guessed the same character than we will tell then that they have entered the same letter again
    if input_letter in already_guessed:
        print(f"You already have guessed {input_letter}...")
        continue
    else:
        already_guessed.add(input_letter)
        
    # if the guessed word is wrong then we will decrease life by 1.
    if input_letter not in chosen_word_list:
        life -= 1
        print(f"You guessed {input_letter}, that's not in the word. You lose a life. Lives remaining: {life}")
        
    else:
        my_indices = []
        # we will fetch the indices where the guessed letter matches with the letter in original word
        for i in range(len(chosen_word_list)):
            if input_letter == chosen_word_list[i]:
                my_indices.append(i)
        
        # print(my_indices)
        # we will replace the '_'(underscore(s)) with the guessed letter
        for i in my_indices:
            guessing_word_list[i] = input_letter
            
        # print(guessing_word_list)
        final_word = ''.join(guessing_word_list)
        
        
        if '_' not in final_word:
            print(f"Congratulations! You win with {life} life(s) left.")
            print(f'And the final word is "{final_word}".')
            break
        
        
    
    
    print(final_word)
    print(stages[life])
    if life == 0:
        print('You lose. Better luck next time...')