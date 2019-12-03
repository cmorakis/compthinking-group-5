# -*- coding: utf-8 -*-
"""

12/5/19
Amber Cocchiola, Chris Morakis, Lincoln Haltrich, Alissha Wilson, and Sarah Jones
DUE: Dec 5
DSCI: 15310
Section 003

This program will find recipes based on categories or by ingredients.
"""

#test input values I used: soy sauce and bean sprouts, bananas and sour milk


#start of program
print(__doc__) 
print(" ")

 
#asks user what route they want to choose to find a recipe
action = input("Would you like to find recipes based on ingredient or categories? Please type response as listed in the question.\n") 

#for recipe by category, go to categories.py file
if action == 'categories':
    import categories  
#for recipe by ingredient, go to ingredient.py file
elif action == 'ingredient':   
    import ingredient 
else:
    print("Restart the program and please type only one of the two options.\n")
    
