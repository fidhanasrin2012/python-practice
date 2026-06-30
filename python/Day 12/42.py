#count vowels and consonants

text = input("Enter a string:")
vowels = 0
consonants = 0
for ch in text:
    if ch.isalpha():
        if ch in "aeiou":
            vowels +=1
        else:
            consonants +=1
print("vowels:",vowels)
print("consonants:",consonants)