# Rosendo Lugo Jr.
# Chapter 6 Programming
# Personal Web Page Generator
import webbrowser


def main():
    def get_name():
        # Inputting the user's name
        name = input("Enter your name: ")
        return name

    def get_age():
        try:
            # Inputting the user's age
            age = int(input("Enter your age: "))
            if age == int:
                print('Hi')
        except:

            file = open('page5.html')
            replaced_content = ""
            line_number = 8
            i = 0

            for line in file:
                line = line.strip()
                if i == line_number:
                    new_line = line.replace("None", '18')
                else:
                    new_line = line
                replaced_content = replaced_content + new_line + "\n"

                i = i + 1
            file.close()
            write_file = open('page5.html', 'w')
            write_file.write(replaced_content)
            write_file.close()
            print('Error: Non-numeric data enter. Default age will be 18 years.')
        else:
            return age

    def get_description():
        # User describes himself
        description = input("Describe yourself: ")
        return description

    def web_page():
        name = get_name()
        age = get_age()
        description = get_description()
        # Open the HTML file on write mode
        file = open("page5.html", 'w')
        file.write("<html>\n")                  # Start html
        file.write("<head>\n")                  # Open the head tag
        file.write("</head>\n")                 # Close the head tag
        file.write("<body>\n")                  # Open the body
        file.write("<center>\n")                #
        file.write("<h1>" + name + "</h1>\n")   # Add the name
        file.write("</center>\n")               # Create a center tag
        file.write("<p>\n")                     # Open the paragraph tag
        file.write(f' I am {age} years old.\n')   # Add the age
        file.write("<p/>\n")                    # Close the paragraph tag
        file.write("<p>\n")                     # Open the paragraph tag
        file.write(" " + description + "\n")    # Add the description
        file.write("<p/>\n")                    # Close the paragraph tag
        file.write("</body>\n")                 # Close the body
        file.write("</html>\n")                 # End html
        webbrowser.open_new_tab("page5.html")
    return web_page()


# Close the main function.
if __name__ == '__main__':
    main()