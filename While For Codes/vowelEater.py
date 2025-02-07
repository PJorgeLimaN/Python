# Prompt the user to enter a word
# and assign it to the user_word variable.
word = input("Write your word.\n>")
user_word = word.upper()
word_without_vowels = ''

for letter in user_word:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else: word_without_vowels += letter
    # Complete the body of the for loop

print(word_without_vowels)

