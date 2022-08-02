#Write a Python program to remove unwanted characters from a given string.
#Sample Output:
#Original String : Pyth*^on Exercis^es
#After removing unwanted characters:
#Python Exercises
#Original String : A%^!B#*CD

special_chars = ['*','^']
abc_string = "  Pyth*^on Exercis^es "
print("Original String : " + abc_string)

for i in special_chars:
    abc_string = abc_string.replace(i, '')
print(abc_string)    

