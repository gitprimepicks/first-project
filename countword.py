# Counting the number of words and spaces and vowelsAND SPACES AND VOWELS
countv=0
countw=0
counts=0

input_sentence=input("tape text :")
sentence=input_sentence.lower()
vowles=["a","e","i","o","u"]
for char in sentence:
    if char in vowles:
        countv=countv+1
    if(char.isspace()):
        counts=counts+1

countw = len(input_sentence.split())

print(" count of vowels", countv)
print(" count of words", countw)
print(" count of spaces", counts)
