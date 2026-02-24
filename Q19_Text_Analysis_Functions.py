#count words in text using len and split function
def countwords(text):
    return len(text.split())

#count vowels in text by summing chars in a set of vowels
def countvol(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

#count consonants by summing chars that are alphabets but not vowels
def countconst(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)

#reverse text using slicing
def revtext(text):
    return text[::-1]

#check if text is palindrome by comparing it to its reverse text
def ispalindrome(text):
    text1 = text.replace(" ", "").lower() #if any spaces or upper case to be removed
    return text1 == text1[::-1]

#remove vowels by joining chars that are not volwels
def removevol(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)

#count freqency of every word in text
def wordfreq(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

#get longest word
def longestword(text):
    words = text.split()
    if not words: return ""
    return max(words, key=len)

def analyze(text):
    print("\n=== TEXT ANALYSIS ===")
    print(f"Words: {countwords(text)}")
    print(f"Vowels: {countvol(text)}")
    print(f"Consonants: {countconst(text)}")
    print(f"Reversed: {revtext(text)}")
    print(f"Palindrome: {'Yes' if ispalindrome(text) else 'No'}")
    print(f"Without vowels: {removevol(text)}")
    
    longest = longestword(text)
    print(f"Longest word: {longest} ({len(longest)} letters)")
    freq = wordfreq(text)
    freq_str = ", ".join([f"{k}: {v}" for k, v in freq.items()])
    print(f"Word Frequency: {freq_str}")

# enter the text to analyze
text= input("Enter text: ")
analyze(text)
