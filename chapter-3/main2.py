# Rosendo Lugo Jr.
# Chapter 3 Programming
# Restaurant Selector project

veg1 = "Main Street Pizza Company" # Vegetarian
veg2 = "Corner Cafe"               # Vegetarian
veg3 = "Mama's Fine Italian"       # Vegetarian
veg4 = "The Chef's Kitchen"        # Vegetarian
vegan1 = "Corner Cafe"              # Vegan
vegan2 = "The Chef's Kitchen"       # Vegan
glu1 = "Main Street Pizza Company"  # Gluten-Free
glu2 = "Corner Cafe"                # Gluten-Free
glu3 = "The Chef's Kitchen"         # Gluten-Free

# Find out if any of your friends have dietary restrictions.
vegetarian = input('Is anyone in your party a vegetarian? ')
vegan = input('Is anyone in your party a vegan? ')
gluten_free = input('Is anyone in your party a gluten-free? ')
print('Here are your restaurant choices:')

if vegetarian == 'yes' or 'Yes':
        if vegan == 'yes' or 'Yes' and gluten_free == 'yes' or 'Yes':
            print(f'    {veg1}\n    {veg2}\n    {veg4}')
        else:
            if gluten_free == 'yes' or 'Yes':
                print(f'    {veg1}\n    {glu2}\n    {glu3}')
            else:
                    print(f'    {veg2}\n    {veg4}')
else:
    if vegan == 'yes' or 'Yes' and gluten_free == 'yes' or 'Yes':
        print(f'    {vegan1}\n  {vegan2}')
    else:
        if gluten_free == 'yes' or 'Yes':
            print(f'    {veg1}\n')