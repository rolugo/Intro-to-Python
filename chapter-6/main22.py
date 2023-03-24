# Rosendo Lugo Jr.
# Chapter 6 Programming
# Personal Web Page Generator
import webbrowser


def main():
    # Inputting the user's name
    name = input("Enter your name: ")

    # Open the HTML file on write mode
    file = open("page5.html", 'w')
    file.write("<html>\n")                  # Start html
    file.write("<head>\n")                  # Open the head tag
    file.write("</head>\n")                 # Close the head tag
    file.write("<body>\n")                  # Open the body
    file.write("<center>\n")                # Create a center tag
    file.write("<h1>" + name + "</h1>\n")   # Add the name
    file.write("</center>\n")               # Close the center tag and keeps it to the left

    try:
        # Inputting the user's age
        age = int(input("Enter your age: "))
        if age != int:
            file.write("<p>\n")  # Open the paragraph tag
            file.write(f'I am {age} years old.\n')  # Add the age
            file.write("<p/>\n")  # Close the paragraph tag

    except ValueError:
        print('Error: Non-numeric data enter. Default age will be 18 years.')
        default_age = 18
        file.write("<p>\n")  # Open the paragraph tag
        file.write(f'I am {default_age} years old.\n')  # Add the default age if a string is inputted.
        file.write("<p/>\n")  # Close the paragraph tag
    else:
        pass

    # User describes himself
    description = input("Describe yourself: ")
    file.write("<p>\n")                     # Open the paragraph tag
    file.write(" " + description + "\n")    # Add the description
    file.write("<p/>\n")                    # Close the paragraph tag
    file.write("</body>\n")                 # Close the body
    file.write("</html>\n")                 # End html
    file.close()                            # Close the file
    webbrowser.open_new_tab("page5.html")   # Display the code in a web browser.


# Close the main function.
if __name__ == '__main__':
    main()