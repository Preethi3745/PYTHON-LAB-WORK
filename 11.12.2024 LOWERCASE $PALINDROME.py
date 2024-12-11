#COUNT LOWERCASE AND UPPERCASE:

a=input("Enter the word: ")
upp=0
low=0
for char in a:
    if char.isupper():
        upp+=1
    elif char.islower():
        low+=1
print("Uppercase count is: ",upp)
print("Lowercase count is: ",low)


#PALINDROME:

a = input("Enter a string: ")
a ==a.replace(" ", "").lower()


reversed_a = ""
for char in a:
    reversed_a = char + reversed_a
if a == reversed_a:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
