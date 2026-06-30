#count frequency of each character


text = input("Enter a string : ")
for ch in set(text):
    print(ch, ":",text.count(ch))