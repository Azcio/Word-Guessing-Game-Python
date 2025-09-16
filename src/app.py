import random #import random to use random.choice() function which can pick a random value

#List called Words will store the values that can randomly be selected
#Words = ['python', 'apple', 'software', 'game', 'challange', 'coding', 'family']

wordfile = "data/filtered_Words.txt" #varaible with filteredwords file

with open(wordfile, 'r') as f: #open the file (f) and read (r)
    filtered_word_list = f.read().splitlines() #turn the file into a list and store in filtered_word_list

def wordSelector(): #Function to select a random word from the List Words using random.choice()
    return random.choice(filtered_word_list)

def display_progress(word, guess): #create list called guessed_letters to store users input
     # Case 1: no guess yet → return all underscores
    if not guess:
        return " ".join("_" for _ in word)

    # Case 2: user made a guess → show correct letters in correct positions
    return " ".join(
        user_letter if user_letter == correct_letter else "_"
        for user_letter, correct_letter in zip(guess, word)
    )

def play_game(): 
    word = wordSelector() #create a variable called word which will call and run wordSelector function and store the output(random word)
    guessed_letters = set() #create a set that will store the users guesses as sets doesn't allow replicated values
    attempts = 5 # max guesses allowed

    print("Welcome to Wordle")
    print(display_progress(word, ""))
    
    while attempts > 0:
        guess = input(f"Guess a {len(word)} word: ").lower()
        
        # Validation
        #isalpha checks that the input is only letters, len(guess) !=1 ensures only the same of char as the selected word is inputted
        if not guess.isalpha() or len(guess) !=len(word):
            print(f"⚠️ Please enter a word with {len(word)} letters.")
            continue #sktip the rest of the loop and asks for input if validation failed
        if guess in guessed_letters: #if the user inputted a letter already in the set guessed_letters
            print("⚠️ You already guessed that.")
            continue # skip the loop and ask for input again
        
        guessed_letters.add(guess) #add guess/input into the set guessed_letters
        
        if guess in word: #If the guessed letter is in the word → print success
            print("✅ Good guess!")
        else:
            attempts -= 1 #else subtract 1 from attempts and print remaining attempts
            print(f"❌ Wrong guess! Attempts left: {attempts}")
        
        progress = display_progress(word, guess) #recall the display function with the updated guessed_Letters
        print(progress)
        
        # Win condition
        if "_" not in progress:
            print("🎉 Congrats! You guessed the word:", word)
            break #break and exit the loop
    else: #else if the word was not guessed then end the loop
        print("💀 Out of attempts! The word was:", word)

if __name__ == "__main__":
    play_game()