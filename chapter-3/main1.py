# Rosendo Lugo Jr.
# Chapter 3 Programming
# Restaurant Selector project

# Find out if any of your friends have dietary restrictions.
print('Enter "Yes or No"')
vegetarian = input('Is anyone in your party a vegetarian? ')
vegan = input('Is anyone in your party a vegan? ')
gluten_free = input('Is anyone in your party a gluten-free? ')

# Determine what restaurant best fits the group.
if vegetarian == 'Yes':
    print("Main Street Pizza Company\n" + "Corner Cafe\n" +
          "Mama's Fine Italian\n" + "The Chef's Kitchen\n")
elif vegan == 'Yes':
        print('Corner Cafe\n' + "The Chef's Kitchen\n")
elif gluten_free == 'Yes':
            print('Main Street Pizza Company\n' + "The Chef's Kitchen\n" )
else:
    print("Joe's Gourmet Burgers")