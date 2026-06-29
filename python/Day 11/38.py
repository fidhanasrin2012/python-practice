#Check whether two strings are anagrams

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not an Anagram")