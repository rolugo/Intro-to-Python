# Rosendo Lugo Jr.
# Chapter 6 Programming
# Personal Web Page Generator
import os
import webbrowser


def main():

    def get_age():
        try:
            # Inputting the user's age
            age = int(input("Enter your age: "))
            if age == int:
                return age
            else:
                # Get the search value and the new age.
                search = 'None'
                default_age = 10

                # Open the original file.
                file = open('page3.html', 'r')

                # Open the temporary file.
                temp_file = open('page_temp.html', 'w')

                # Read the quantity field.
                age = file.readline()

                # Write either this record to the temporary file,
                # or the new record if this is the one that is
                # to be modified.
                if age == search:
                    # Write the modified record to the temp file.
                    temp_file.write(f'{default_age}\n')

                else:
                    # Write the original record to the temp file.
                    temp_file.write(f'{age}\n')

                # Close the coffee file and the temporary file.
                file.close()
                temp_file.close()

                # Delete the original coffee.txt file.
                os.remove('page3.html')

                # Rename the temporary file.
                os.rename('page_temp.html', 'page3.html')
                webbrowser.open_new_tab("page3.html")

            return age
        except ValueError:
            print('Error: Non-numeric data enter. Default age will be 18 years.')

    def get_description():
        # User describes himself
        description = input("Describe yourself: ")
        return description

    def web_page():
        age = get_age()
        description = get_description()

        # Open the HTML file on write mode
        file = open("page3.html", 'w')
        file.write("<html>\n")                  # Start html
        file.write("<head>\n")                  # Open the head tag
        file.write("</head>\n")                 # Close the head tag
        file.write("<body>\n")                  # Open the body
        file.write("<p>\n")                     # Open the paragraph tag
        file.write(f' I am {age} years old.\n')   # Add the age
        file.write("<p/>\n")                    # Close the paragraph tag
        file.write("<p>\n")                     # Open the paragraph tag
        file.write(" " + description + "\n")    # Add the description
        file.write("<p/>\n")                    # Close the paragraph tag
        file.write("</body>\n")                 # Close the body
        file.write("</html>\n")                 # End html
        webbrowser.open_new_tab("page3.html")
    return web_page()


# Close the main function.
if __name__ == '__main__':
    main()