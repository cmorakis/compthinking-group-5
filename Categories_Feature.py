# -*- coding: utf-8 -*-
"""

11/26/2019
Fine Dining
DSCI: 15310
003

"""

import pandas as pd

#kind of just put this here I dont know why, I wanted to use it to make adding the information easier
Cat = pd.read_csv('recipes.csv')
Categories = Cat['Title'].tolist()

#(From Here)I Just made Variables of sorta test lists by turning random recipes into dataframes
Cake = {'Cakes': ["BlueBerry Coffee Cake", "Banana Cake", "Blueberry Coffee Cake", "Chocolate Cake", "Chocolate Mayonaise Cake", 
"Crazy Cake",
"Fresh Pear Cake",
"Graham Cracker Cake",
"Hot Water Chocolate Cake",
"Hungry Bear Cheese Cake",
"Lemon Poppy Cake",
"Light Old Fashioned Fruit Cake",
"Oatmeal Cake",
"Orange Angel Food Cake",
"Orange-Poppy Seed Pound Cake",
"Pineapple Cake",
"Pineapple-Carrot Cake",
"Potatoe Cake",
"Pumpkin Swirl Cheesecake",
"Refrigerator Cheesecake",
"Sherry Wine Cake",
"Special Prune Cake",
"Spicy Fruit and Nut Cake",
"Three Layer Chocolate Mayonnaise Cake",
"Two Layer Chocolate Mayonnaise Cake",
"Upside Down Cake",
"Saucy Shrimp Over Chinese Noodle Cakes",
"Hungry Bear Cheese Cake",
"Crisp Potato Pancakes"
]}

Cakes = pd.DataFrame(Cake)

Meat = {'Meats': ["Maryland Fried Chicken"]}

WeHaveTheMeats = pd.DataFrame(Meat)

Veg = {'Vegtables': ["Glazed Carrots"]}

Veggie = pd.DataFrame(Veg)

Sp = {'Soups': ["MineStrone Soup"]}

Y = pd.DataFrame(Sp)
#(To Here)

#I setup the category process here for being able to select a category of currently four recipe ranges
Cats = ['Cake', 'MeatBase', 'VegetableBase', 'Soup']
C = input('What is on your mind?\n')

if C in Cats:
    print(f'A {C} recipe what a delicous choice! Here is what I have.')
else:
    print(f'Im sorry but I do not know what kind of meal {C} is.')

#Once a category is decided this will print the list that is requested
if C == 'Cake':
    print(Cakes)
elif C == 'MeatBase':
    print(WeHaveTheMeats)
elif C == 'VegtableBase':
    print(Veggie)
elif C == 'Soup':
    print(Y)
