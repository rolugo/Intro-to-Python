# Rosendo Lugo Jr.
# Chapter 6 Programming
# Personal Web Page Generator

def main():
    # Inputting the user's age
    age = int(input("Enter your age: "))
    if age != int:
        print('Not good!')
    else:
        print('Wow')

    description = input("Describe yourself: ")

    try:
        # Open the HTML file on write mode
        file = open("page3.html", 'w')
        file.write("<html>\n")                  # Start html
        file.write("<head>\n")                  # Open the head tag
        file.write("</head>\n")                 # Close the head tag
        file.write("<body>\n")                  # Open the body
        file.write("<p>\n")                     # Open the paragraph tag
        file.write(f'I am {age} years old.\n')   # Add the age
        file.write("<p/>\n")                    # Close the paragraph tag
        file.write("<p>\n")                     # Open the paragraph tag
        file.write(" " + description + "\n")    # Add the description
        file.write("<p/>\n")                    # Close the paragraph tag
        file.write("</body>\n")                 # Close the body
        file.write("</html>\n")                 # End html
    except Exception as err:
        print(err)
    finally:
        print('Continue')


# Close the main function.
if __name__ == '__main__':
    main()