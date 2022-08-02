#Write a Python program to remove unwanted characters from a given string.
#Sample Output:
#Original String : Pyth*^on Exercis^es
#After removing unwanted characters:
#Python Exercises
#Original String : A%^!B#*CD

special_chars = ['*','^','%','!','#']
abc_string = "  Pyth*^on Exercis^es "
xyz_string = " A%^!B#*CD "
print("Original String : " + abc_string)
print("Second Original String: " + xyz_string)

for i in special_chars:
    abc_string = abc_string.replace(i, '')
    xyz_string = xyz_string.replace(i, '')
print("After removing unwanted characters:",abc_string)  
print("After removing unwanted characters:",xyz_string)  
