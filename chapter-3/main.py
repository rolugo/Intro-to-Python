# Rosendo Lugo Jr.
# Chapter 3 Programming
# Restaurant Selector project

# Restaurant Choices
choice1 = "Joe's Gourmet Burgers"       # NO vegetarian, vegan, or gluten-free
choice2 = "Main Street Pizza Company"   # Vegetarian and gluten-free
choice3 = "Corner Cafe"                 # Vegetarian, vegan, and gluten-free
choice4 = "Mama's Fine Italian"         # Vegetarian
choice5 = "The Chef's Kitchen"          # Vegetarian, vegan, and gluten-free


# Find out if any of your friends have dietary restrictions.
print('Enter "yes or no"')
vegetarian = input('Is anyone in your party a vegetarian? ')
vegan = input('Is anyone in your party a vegan? ')
gluten_free = input('Is anyone in your party a gluten-free? ')
print('Here are your restaurant choices:')

# Determine what restaurant best fits the group
# using Boolean variables.
if vegetarian == 'yes' and vegan == 'yes' and gluten_free == 'yes':
    veg_vegan_glu = True
else:
    veg_vegan_glu = False
if vegetarian == 'yes' and vegan == 'yes' and gluten_free == 'no':
    veg_vegan = True
else:
    veg_vegan = False
if vegetarian == 'yes' and vegan == 'no' and gluten_free == 'yes':
    veg_glu = True
else:
    veg_glu = False
if vegetarian == 'yes' and vegan == 'no' and gluten_free == 'no':
    veg = True
else:
    veg = False

# Print based on the restaurant choices.
if veg_vegan_glu:
    print(f'    {choice3}\n    {choice5}')
elif veg_vegan:
    print(f'    {choice3}\n    {choice5}')
elif veg_glu:
    print(f'    {choice2}\n    {choice3}\n    {choice5}')
elif veg:
    print(f'    {choice4}')
else:
    print(f'    {choice1}')