Imported_word_file = "data/10000-english-words.txt" #create a variable to find path to the word txt file

try: #try to run the code and if something goes wrong, it jumps to the except
    with open(Imported_word_file, 'r') as f: #open the file as f in read mode (r)
        print("File opened successfully!")
        print(f.readline())  # prints the first line to verify content
except FileNotFoundError: #If the file isn’t there, this block runs
    print("File not found. Check the path!")

#function to filter words to just 5-10 letter words
def filterwords(word_list): #create a list variable to store the words
    filtered_Words = [word for word in word_list if 5 <= len(word) <= 10] #for loop through every loop word in word list
    return filtered_Words #return new list with words with 5-10 letters

#check to see if new wordlist filtered properly
with open(Imported_word_file, 'r') as f: #read (r) the file (f)
    words = f.read().splitlines() #.splitlines() used to spliut string into a list of lines (each line = one word)

#cakk the filterwords function
filtered_words = filterwords(words) #pass words list into the function
print(filtered_words[:10]) #check to see if filter worked

with open ("filtered_Words.txt", "w") as f:
    f.write("\n".join(filtered_words))