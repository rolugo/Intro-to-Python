# Rosendo Lugo Jr.
# Chapter 6 Programming
# Personal Web Page Generator

def web_page(name, age, description):

    try:
        # Open the HTML file on write mode
        file = open("page.html", 'w')
        file.write("<html>\n")  # Start html
        file.write("<head>\n")  # Open the head tag
        file.write("</head>\n")  # Close the head tag
        file.write("<body>\n")  # Open the body
        file.write("<center>\n")  #
        file.write('<h1>{}</h1>\n'.format(name))  # Add the name
        file.write("</center>\n")  # Create a center tag
        file.write("<p>\n")  # Open the paragraph tag
        file.write(f'I am{}years old.\n'.format(age))  # Add the age
        file.write("<p/>\n")  # Close the paragraph tag
        file.write("<p>\n")  # Open the paragraph tag
        file.write('{}\n'.format(description))  # Add the description
        file.write("<p/>\n")  # Close the paragraph tag
        file.write("</body>\n")  # Close the body
        file.write("</html>\n")  # End html

        file.close()
        return True
    except:

        return False

def main():
    name = ''
    description = ''
    age = ''
    # Inputting the user's name
    name = input("Enter your name: ")
    # Inputting the user's age
    age = int(input("Enter your age: "))
    # User describes himself
    description = input("Describe yourself: ")

    print('Hi')
    if web_page(name, age, description):
        print('Done!')
    else:
        print('Error: Non-numeric value enter: {}'.format(page.html))



# Close the main function.
main()