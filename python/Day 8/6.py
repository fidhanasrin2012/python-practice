#Count vowels

def count_vowels(text):
    count = 0 
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

word = input("Enter a text:")
print("Number of vowels =",count_vowels(word))