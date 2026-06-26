#Reverse a String

def reverse_string(text):
    return text[:: -1]
word= input("Enter a text:")
print("Reversed String :",reverse_string(word))