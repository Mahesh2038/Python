import random, listOfWords, stages

chosen_word = random.choice(listOfWords.words_list)
display = []
for word in chosen_word:
    display += "_"
#print(chosen_word)
end_of_game = False
lives = 6
while end_of_game != True:
    print(display)
    guess_letter = input("Guess the letter ")
    
    if guess_letter in display:
        print(f"You already guessed '{guess_letter}'")

    for let_num in range(len(chosen_word)):
        if chosen_word[let_num] == guess_letter:
            display[let_num] = guess_letter
            print(stages.stage[lives])

    if guess_letter not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess_letter}', not in word, you lost a life. Remaining lives {lives}")
        print(stages.stage[lives])
        if lives == 0:
            print(f"game over, You lose\nThe word is '{chosen_word}'")
            end_of_game = True
    #print(display)
    if "_" not in display:
        final_word = ''.join(display)
        print(f"Finally you guessed it right!, The word is '{final_word}'")
        print("You Win!!!")
        end_of_game = True
    
    