# Rosendo Lugo Jr.
# Chapter 6 Programming
# Personal Web Page Generator

def main():
    try:
        # Inputting the user's name
        name = input("Enter your name: ")
        # Inputting the user's age
        age = int(input("Enter your age: "))
        # User describes himself
        description = input("Describe yourself: ")


        # Open the HTML file on write mode
        file = open("page.html", 'w')
        file.write("<html>\n")                  # Start html
        file.write("<head>\n")                  # Open the head tag
        file.write("</head>\n")                 # Close the head tag
        file.write("<body>\n")                  # Open the body
        file.write("<center>\n")                #
        file.write("<h1>" + name + "</h1>\n")   # Add the name
        file.write("</center>\n")               # Create a center tag
        file.write("<p>\n")                     # Open the paragraph tag
        file.write(f'I am {age} years old.\n')   # Add the age
        file.write("<p/>\n")                    # Close the paragraph tag
        file.write("<p>\n")                     # Open the paragraph tag
        file.write(" " + description + "\n")    # Add the description
        file.write("<p/>\n")                    # Close the paragraph tag
        file.write("</body>\n")                 # Close the body
        file.write("</html>\n")                 # End html

    except ValueError:
        print('Non-numeric data enter. Default age will be 18 years.')
    finally:
        print('Hi')


    # Close the main function.
if __name__ == '__main__':
    main()