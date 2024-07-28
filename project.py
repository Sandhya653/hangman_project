import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
print(chosen_word)
word_length=len(chosen_word)
lives=6
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
display = []
for _ in range(word_length):
    display += "_"
print(display)

end_of_the_game=False
while not end_of_the_game:
    guess=input("Guess a letter? \n").lower()
    for position in range(word_length):
        letter = chosen_word[position]
    
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives-=1    
        if lives ==0:
            end_of_the_game=True
            print("YOU LOOSE!")    
    print(display)
    
    if '_' not in display:
        end_of_the_game=True
        print("You won!")

    print(stages[lives])