# Step 1

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable named chosen_word.
import random
word_list = ['abhishek','hetal','bhavik','maitri','amit','krishna','ami','umang','vaibhavi','kalyani','madhavi','nilesh','chetan','chirag','paras','tushar','vishal','nikit','anjali','drashti','parth','kuki','abhay','tirth','dhimant','jaymit','devangi','krupali']

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''





# random_int = random.randint(0,len(word_list)-1)
# chosen_word = word_list[random_int]
# instead of above two lines do the following line
chosen_word = random.choice(word_list)


print(chosen_word)


print(logo)


# TODO-2 - Ask The user to guess a letter and assign their answer to a variable called guess. make the guess lowercase.


life = 6

final_word = '_'*len(chosen_word)
final_word_list = list(final_word)

already_guessed = set()


while life >0:
    
    guess = input("Guess a letter: ").lower()


    if guess in already_guessed:
        print(f"You already have guessed {guess}.")
        continue
    else:
        already_guessed.add(guess)
        

# print(guess)


    # TODO-3 - Check if the letter the user guessed(guess) is one of the letter in the chosen_word 
    # trying = '_'*len(chosen_word)
    # trying_list = list(trying)


    
    
    
      
    
    
    # if trying.count("_") == len(chosen_word):
    #     life -=1
    # elif final_word.count("_") == 0:    
    #     print("You win!!")
    # elif life == 0:
    #     print("You lose")
    
    
    
    
    # chosen_word_list = []
    # for i in chosen_word:
    #     chosen_word_list.append(i)
    # Rather use below
    chosen_word_list = list(chosen_word)
    
    
    
    if guess not in chosen_word_list:
    # if guess in chosen_word_list:
    #     for i in guess:
    #         for j in chosen_word:
    #             if i == j:
    #                 trying += i
    #             else:
    #                 trying += "_"
    # else:
        print(f"You guessed {guess}, that's not in the Word. You lose a life. Lives remaining: {life-1}")
        life -= 1
    
        if life == 0:
            print("You are out of lives. \nYou lose, better luck next time...")
        
        
    
    
    
    my_indices =[]
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            my_indices.append(i)
    
    for i in my_indices:
        final_word_list[i] = guess
    
    final_word = ''.join(final_word_list)
    
    print(final_word)
    if "_" not in final_word_list:
        print("Congratulations!! You win")
        print(stages[life])
        break
    print(stages[life])
    