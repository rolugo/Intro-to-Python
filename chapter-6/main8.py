# Rosendo Lugo Jr.
# Chapter 6 Programming
# Personal Web Page Generator

def main():

    try:
        # Inputting the user's age
        age = int(input("Enter your age: "))
        if age == int:
            print('Error')
    except:
        print('Error: Non-numeric data enter. Default age will be 18 years.')
        file = open('page4.html', 'w')
        file.write(f'I am 18 years old.\n')
        file.close()
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
    finally:
        print('Continue')

# Close the main function.
if __name__ == '__main__':
    main()

    #default_age = 18
    #file = open('page5.html', 'rt')
    #temp_file = open('page5.html', 'wt')
    #for line in file:
        #temp_file.write(line.replace('I am gg years old.', f'I am {default_age} years old.\n'))
    #file.close()
    #temp_file.close()