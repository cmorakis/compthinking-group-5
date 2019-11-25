# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:57:51 2019

9/24/19
Amber Cocchiola
DUE: Nov 5
DSCI: 15310
Section 003


"""

#recipe file from Github
#https://github.com/cweber/cookbook/blob/master/recipes_forimport.csv
#used as base recipe data for educational purpose

#test input values I used: eggs (as single element), sour milk (as single element), sour milk and banana



import pandas

#defining fucntions
def print_recipe(index):
    """print_recipe will print the full recipe from the dictionary of recipes to the screen. It accepts one integer argument. """
#    lowidx = index
    upidx = index
    #this loop finds where the recipe starts
#    while lowidx >= 0:
#        if pandas.isna(recipes['Title'][lowidx]):
 #           lowidx = lowidx - 1
  #      else:
   #         print("\n", recipes['Title'][lowidx])  
    #        break 
    #this loop finds where the recipe ends
    while upidx <= 2090:
        if pandas.isna(recipes['Title'][upidx]):
            upidx = upidx + 1
        else:
            break   
    #prints recipe based on found bounds
    print(recipes['Title'][index])
    for j in range(index, upidx):
        if pandas.isna(recipes['Directions'][j]) == False:
            print(recipes['Directions'][j], "\n")
    for i in range(index, upidx):
        if pandas.isna(recipes['Quantity'][i]) == False:
            print(recipes['Quantity'][i])
        if pandas.isna(recipes['Unit of Measure'][i]) == False:
            print(recipes['Unit of Measure'][i])
        if pandas.isna(recipes['Ingredient'][i]) == False:
            print(recipes['Ingredient'][i])
        print()

def find_recipetitle(index):
    """find_recipetitle will find the name of a dish given an ingredient. It accepts one integer argument. """
    lowidx = index
    #this loop finds where the recipe starts
    while lowidx >= 0:
        if pandas.isna(recipes['Title'][lowidx]):
            lowidx = lowidx - 1
        else:
            return(lowidx)  
                    

def all_matches(ingredients):
    """ all_matches finds if all ingredients in the ingredients list or found in a recipie and returns a boolean. It accepts a list argument"""
    for i in range(0, iLength):
        for category, data in recipes.items():
            for key in data:
                if data[key] == ingredients[i]:
                    return 0



print(__doc__)  
          
print("Want to find recipes? Type 'y' for yes and 'n' for no.")
decision = input()
 
  
 #inputting ingredients to list
ingredients = []
 
while decision == 'y':
    print("\nWhat is in your cupboard? Enter one item at a time.")
    item = input()
    ingredients.append(item)
    print("\nWant to add another? Type 'y' for yes. Hit any other key for no.")
    decision = input()
 
    
    
 #adding file of recipes
file_name = 'recipes.csv'

csv_recipes = pandas.read_csv(file_name)
recipes = csv_recipes.to_dict()

#print(csv_recipes)
###for testing if I imported the file correctly^^^

 
#comparing ingredients to recipes
rLength = len(recipes)
iLength = len(ingredients)
matches = []
titleListnum = []
titleListfinal = []

 
for i in range(0, iLength): 
    for category, data in recipes.items():
        for key in data:
            if data[key] == ingredients[i]:
                matches.append(key)

for k in range(0, len(matches)):
    titleListnum.append(find_recipetitle(matches[k]))
    
titleListnum.sort()

for p in range(0, len(titleListnum)-1):
    if titleListnum[p] == titleListnum[p+1]:
        titleListfinal.append(titleListnum[p])
    
#outputting matches
print("\n", print_recipe.__doc__)
for j in range(0, len(titleListfinal)):
    print_recipe(titleListfinal[j])
    
    
#for q in range(0, len(matches)):
    #print(find_recipetitle(matches[q]))
    
