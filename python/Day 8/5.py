#Check Palindrome

def palindrome(text):
    if text == text [:: -1]:
        return True
    return False

word = input("Enter a text:")
if palindrome(word):
    print("Is palindrome")
else:
    print("Not Palindrome")