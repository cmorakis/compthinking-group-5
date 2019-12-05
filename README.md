# compthinking-group-5

Amber Cocchiola
Chris Morakis
Lincoln Haltrich
Sarah Jones
Alissha Wilson


The final project is in the "Final" branch. It requires four files to run (FineDiningMain.py, ingredient.py, category.py, and recipes.csv).

FineDiningMain.py needs to be run in order to use the complete program. The rest of the files are all used in the 'main' file.

The purpose of the program is to print recipes for the user. The user has two options to do this. They can use: search by ingredient or search by category. Search by category will have the user pick a cateogry of food and select a recipe they want to see. Search by ingredient has the user input ingredients and gives recipes based on whether the recipe contians the user specified ingreidents.



Categories:



Ingredient:
Input: ingredient (one at a time)
Output: List of recipes printed to console
The recipes are imported from recipes.csv and are stored as a dictionary in a dictionary. The program compares user input to the section in the nested loop 'ingredient'. It then uses the indexes provided by the dictionary structure to find the title associated with the ingredient and compares the titles to find 'best matches' versus 'okay matches'. 'Best matches' uses two or more of the ingredients provided and 'okay matches' are recipes that use one of the ingredients provided. Both 'best matches' and 'okay matches' are provided to the user as an output.
