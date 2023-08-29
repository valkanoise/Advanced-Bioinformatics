"""
Exercise 3:
    
Choose (or create) a text file (it can be a sheet of your thesis plan, a paper 
or whatever whatever), write a program that: i) reads the file, and ii) then 
extracts the number of times it a given word appears (chosen by the user) and 
print it on the screen
    
"""

def count_word_occurrences(file_content, word):
    word = word.lower()
    words = file_content.lower().split()
    return words.count(word)

# Replace 'your_file.txt' with the path to your text file
file_path = './Random_text.txt'

try:
    with open(file_path, 'r') as file:
        file_content = file.read()
        user_word = input("Word to count in the file: ")
        occurrences = count_word_occurrences(file_content, user_word)
        print(f"The word '{user_word}' appears {occurrences} times in the file.")

except FileNotFoundError:
    print(f"File '{file_path}' not found.")

