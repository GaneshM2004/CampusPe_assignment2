# Ask user for a sentence and display various string operations
sentence = input("Enter a sentence: ")
print("Original: " + sentence)

#using len() function to get no. of characters(it includes spaces)
charwspaces= len(sentence)
print("Characters (with spaces): " + str(charwspaces))

#using len() function along with replace() to get no. of characters without spaces
charswospaces = len(sentence.replace(" ", ""))
print("Characters (without spaces): " + str(charswospaces))

#using len() function along with split() to get no. of words in the sentence
words = len(sentence.split())
print("Words: " + str(words))

#upper(), lower(), title() are used to change the case of the sentence
print("UPPERCASE: " + sentence.upper())
print("lowercase: " + sentence.lower())
print("Title Case: " + sentence.title())

#using split() to get the first and last word of the sentence
first_word = sentence.split()[0]
print("First word: " + first_word)

last_word = sentence.split()[-1]
print("Last word: " + last_word)

#using slicing to reverse it
reversed_sentence = sentence[::-1]
print("Reversed: " + reversed_sentence)

#output:
# Enter a sentence: good morning
# Original: good morning
# Characters (with spaces): 12
# Characters (without spaces): 11
# Words: 2
# UPPERCASE: GOOD MORNING
# lowercase: good morning
# Title Case: Good Morning
# First word: good
# Last word: morning
# Reversed: gninrom doog