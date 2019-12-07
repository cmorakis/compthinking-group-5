# -*- coding: utf-8 -*-
"""
11/26/2019
Fine Dining
DSCI: 15310
003
"""

import pandas as pd

Cat = pd.read_csv('recipes.csv')
Categories = Cat['Title'].tolist()

def print_recipe(index):
    """print_recipe will print the full recipe from the dictionary of recipes to the screen. It accepts one integer argument. """
#    lowidx = index
    upidx = index+1
    #this loop finds where the recipe starts
#    while lowidx >= 0:
#        if pandas.isna(recipes['Title'][lowidx]):
 #           lowidx = lowidx - 1
  #      else:
   #         print("\n", recipes['Title'][lowidx])  
    #        break 
    #this loop finds where the recipe ends
    while upidx <= 2090:
        if pd.isna(recipes['Title'][upidx]):
            upidx = upidx + 1
        else:
            break   
    #prints recipe based on found bounds
    print(recipes['Title'][index])
    for j in range(index, upidx):
        if pd.isna(recipes['Directions'][j]) == False:
            print(recipes['Directions'][j], "\n")
    for i in range(index, upidx):
        if pd.isna(recipes['Quantity'][i]) == False:
            print(recipes['Quantity'][i])
        if pd.isna(recipes['Unit of Measure'][i]) == False:
            print(recipes['Unit of Measure'][i])
        if pd.isna(recipes['Ingredient'][i]) == False:
            print(recipes['Ingredient'][i])
        print()

def recipetitle(R):
    for T in range(0,2090):
       if recipes['Title'][T] == R:
           return T
       

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

Meat = {'Meats': ["Maryland Fried Chicken", "Chicken and Shrimp Cantonese",
"Chicken With Pineapple",
"Chinese Beef",
"Chinese Broccoli",
"Chinese Chicken Salad",
"Chinese Fried Rice",
"Chinese Pepper Steak",
"Chinese Roast Pork",
"Chinese Stir Fried Chicken with Peanuts",
"Scallops",
"Golden Nugget Beef",
"Baby Back Ribs",
"Sweet and Sour Meatballs",
"Saucy Shrimp Over Chinese Noodle Cakes",
"Sole Thermidor",
"Bake Trout",
"Cheesy Fish Fillets with Spinach",
"Sauteed Scallops",
"'Louies' Linguini with Clam Sauce",
"Sole Almondie",
"Hot Crab Dip",
"Shrimp Saute",
"Sitr-Fry Beef and Broccoli",
"Barbecued Spareribs",
"Sweet and Sour Pork",
"Beef Scallops with Fresh Tomato Sauce",
"Veal Scallopini",
"Savory Goulash",
"Veal Parmigan",
"Teriyaki Steak",
"Beef Stroganoff",
"Egg Foo Young",
"Egg Roll Filling",
"Egg Roll Wrappers",
"Pineapple Spareribs",
"Pork Fu Man Chow",
"Shrimp Pineapple Fried Rice",
"Sweet and Sour Pork",
"Albert's Chicken",
"Avocado Chicken Melt",
"Batter Fried Chicken",
"Catalina Chicken Stir Fry",
"Chicken Breasts Florentine",
"Chicken Cashew",
"Chicken Lo Mein",
"Chicken Paprika",
"Chicken Schnitzel",
"Chicken with Artichoke",
"Coq au Vin",
"Creamy Chicken Broccoli with Rice",
"In a Hurry Chicken Curry",
"Jack Zucchini Chicken",
"Maryland Fried Chicken",
"Oven Fried Chicken",
"Parsley and Parmasen Baked Chicken",
"Sandra's 'Tree Timmer' Chicken",
"Saute'd Chicken Breats",
"Saute'd Chicken Livers",
"Spicy Singapore Wings",
"Turkey Tenderloin Supreme",
"Beef Enchiladas",
"Beef Spinach Quiche",
"Chicken Tamale Pie"
]}

WeHaveTheMeats = pd.DataFrame(Meat)

Veg = {'Vegtables': ["Glazed Carrots", "Asparagus Stir-Fried",
"Baked Green Beans",
"Baked Zucchini with Mushrooms",
"Bit O' Zucchini Bites",
"Cheesy Spinach Bake",
"Company Cabbage",
"Crisp Potato Pancakes",
"Easy Oven Baked Potatoes",
"Eggplant Rollatini",
"Glazed Carrots",
"Green Beans Salerno",
"Italian Zucchini",
"Orange Sweet Potatoes",
"Peas",
"Saute Zucchini",
"Spinach Pie",
"Spinach Souffle",
"Spinach Strudels",
"Stuffed Zucchini",
"Summer Squash",
"Sweet and Sour Red Cabbage",
"The Spinach",
"Mushrooms in Sour Cream",
"Three Cheese Spinach",
"Tulelake Potato Casserole",
"Zucchini Patties",
"Artichoke-Mozzarella Casserole",
"Asparagus Tomato Quiche",
"Broccoli and Rice Casserole",
"Broccoli Cheese Pie",
"Garden Quiche",
"Wild Mushroom and Spinach Lasanga",
"Zucchini Casserole",
"Cucumbers in Sour Cream",
"Carrot Carousel",
"Coleslaw",
"Zucchini Apple Slaw",
"Chinese Broccoli",
]}

Veggie = pd.DataFrame(Veg)

Sp = {'Soups': ["MineStrone Soup", "Broccoli Cheese Soup",
"Chicken Noodle Soup",
"Cleo's Clam Chowder",
"Creamy Zucchini Mushroom Soup",
"Elephant Stew",
"Hungry Bear Vegetable Soup",
"Mexican Meatball Soup",
"Tortilla Soup",
]}

Y = pd.DataFrame(Sp)

Seafood = {'Seafoods': ["Shrimp Pineapple Fried Rice",
"Beef Scallops with Fresh Tomato Sauce",
"Saucy Shrimp Over Chinese Noodle Cakes",
"Sole Thermidor",
"Bake Trout",
"Cheesy Fish Fillets with Spinach",
"Sauteed Scallops",
"'Louies' Linguini with Clam Sauce",
"Sole Almondie",
"Hot Crab Dip",
"Shrimp Saute",
"Scallops",
"Chinese Noodle Casserole"
]}

Sea = pd.DataFrame(Seafood)

Pie = {'Pies': ["Banana Cream Pie",
"Blackberry Nectarine Pie",
"Creamy Apple Pie",
"Dutch Apple Pie",
"Fresh Strawberry Pie",
"Lemon Cloud Pie",
"Lemon Luscious Pie",
"Lemon Meringue Pie",
"Old Fashioned Apple Pie",
"Peach Almond Pie",
"Peach Parfait Pie",
"Peanut Butter Ice Cream Pie",
"Peanut Butter Pie",
"Pie Crust",
"Sour Cream Raisin Pie",
"Walnut Pie",
"Walnut-Raisin pie",
]}

P = pd.DataFrame(Pie)

Salad = {'Salads': ["Blue Cheese Dressing",
"Broccoli Curry Salad",
"Broccoli Salad",
"Broccoli Salad with Pineapple",
"Carrot Carousel",
"Coleslaw",
"Cranberry Mold",
"Cucumbers in Sour Cream",
"Five Bean Salad",
"Five Cup Salad",
"Garden Vegetable Pasta",
"Green Bean Salad",
"Heavenly Cheese Salad",
"Horseradish Dressing",
"Lemon Cloud Salad",
"Lima Bean Salad",
"Pea Salad",
"School French Dressing",
"Spinach Salad",
"Spinach Salad with Avocado",
"Spinach Salad with Alfalfa Sprouts",
"Summer Fruit Salad",
"Top Ramen Salad",
"Zucchini Apple Slaw"
]}

Sal = pd.DataFrame(Salad)

Sweet = {'Sweets': ["Apple Dumplings",
"Apple Dessert for a Crowd",
"Chilled Prune Whip",
"Fresh Peach Dessert",
"South Carolina Cobbler",
"Spanish Cream Pudding",
"My Best Gingerbread",
"Blue Chip Cookies",
"Bourbon Balls",
"Chocolate Crisp Bran Cookies",
"Chocolate Peanut Brunch Bars",
"Chocolate Trio Squares",
"Christmas Logs",
"Christmas Snowballs",
"Crisp Oatmeal Fruit Strips",
"Frosted Delights",
"Ginger Snap Bars",
"Ginger Snaps",
"Honey Graham Crackers",
"Jello Pastel Cookies",
"Lemon Squares",
"Minties",
"Oatmeal Cookies",
"Oatmeal Fudge Bars",
"Fudge Layer",
"Peanut Butter Cookies",
"Pineapple Graham Bars",
"Prune Nut Bars",
"Pumpkin Oatmeal Cookies",
"Snickerdoodles",
"Soft Sugar Cookies",
"Thumbprint Cookies",
"Walnut Squares",
"Angel Hash",
]}

Swt = pd.DataFrame(Sweet)

#(To Here)

#I setup the category process here for being able to select a category of currently four recipe ranges



Cats = ['Cake', 'cake', 'MeatBase', 'meatbase', 'VegetableBase', 'vegetablebase', 'Soup', 'soup', 'Seafood', 'seafood', 'Pie', 'pie', 'Salad', 'salad', 'Sweet', 'sweet']
print("\nPick from: Cake, Meatbase, VegetableBase, Pie, Salad, Sweet, Seafood or Soup\n")
C = input('What is on your mind? We have Cake, MeatBase, VegetableBase, Soup, Seafood, Pie, Salad, and Sweet.\n')

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
elif C == 'Seafood':
    print(Sea)
elif C == 'Salad':
    print(Sal)
elif C == 'Pie':
    print(P)
elif C == 'Sweet':
    print(Swt)

file_name = 'recipes.csv'

csv_recipes = pd.read_csv(file_name)
recipes = csv_recipes.to_dict()


R = input(f' Which {C} recipe would you like? Please type the specific recipe')

    
print_recipe(recipetitle(R))      
    


    
