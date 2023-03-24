# Rosendo Lugo Jr.
# Chapter 6 Programming
# Personal Web Page Generator
import os


def main():

    try:
        # Inputting the user's age
        age = int(input("Enter your age: "))
        if age == int:
            print('Error')
    except:
        print('Error: Non-numeric data enter. Default age will be 18 years.')
        default_age = 12
        file = open('page4.html')
        temp_file = open('page_temp.html', 'w')
        for line in file:
            temp_file.write(line.replace('None', f'I am {default_age} years old.'))
        file.close()
        temp_file.close()

        os.remove('page4.html')
        os.rename('page_temp.html', 'page4.html')

    else:
        # Open the HTML file on write mode
        file = open("page4.html", 'w')
        file.write("<html>\n")  # Start html
        file.write("<head>\n")  # Open the head tag
        file.write("</head>\n")  # Close the head tag
        file.write("<body>\n")  # Open the body
        file.write("<p>\n")  # Open the paragraph tag
        file.write(f'I am {age} years old.\n')  # Add the age
        file.write("<p/>\n")  # Close the paragraph tag
        file.write("</body>\n")  # Close the body
        file.write("</html>\n")  # End html
        file.close()


# Close the main function.
if __name__ == '__main__':
    main()