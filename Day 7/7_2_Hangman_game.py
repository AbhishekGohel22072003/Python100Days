# Step 1

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable named chosen_word.
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





# random_int = random.randint(0,len(word_list)-1)
# chosen_word = word_list[random_int]
# instead of above two lines do the following line
chosen_word = random.choice(word_list)


# print(chosen_word)


print(logo)


# TODO-2 - Ask The user to guess a letter and assign their answer to a variable called guess. make the guess lowercase.


life = 6

final_word = '_'*len(chosen_word) #Aane while loop ni bahar j initialize karavvo pade nahitar dar vakhte reinitialize thay jethi navo word juna word sathe integrate na thai shake
final_word_list = list(final_word) #tema index pramane words add karva mate string to list ma typecast karyu
# kemke string immutable chhe jyare list mutable chhe

already_guessed = set()
# aane pan bahar j initialize karavvu pade nahitar jo loop ma hoy to dar vakhate set empty thai jay and expected result na male

while life >0:
    
    guess = input("Guess a letter: ").lower() #kemke badha j words lower case ma chhe


    if guess in already_guessed:
        print(f"You already have guessed {guess}.")
        continue
    else:
        already_guessed.add(guess) #jo phelethi set ma hashe to nahi add kare nahitar add kari deshe
        

# print(guess)


    # TODO-3 - Check if the letter the user guessed(guess) is one of the letter in the chosen_word 
    # trying = '_'*len(chosen_word) # aa matr try leva initialise karavyu chhe
    # trying_list = list(trying)


    
    
    
      
    
    
    # if trying.count("_") == len(chosen_word): # ama underscores valo problem aavto hato 
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
        # nichena commented code ni kai jarur j nathi
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
        
        
    
    
    # have je places par guessed letter hashe teni index my_indices ma store thashe and te mujab final_word_list ma '_' ni jagya e guess je hashe te aavi jashe
        
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