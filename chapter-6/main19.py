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
            print('Error: Non-numeric data enter. Default age will be 18 years.')
            list_of_age = []
            with open("page5.html", "r") as file:
                for line in file.readline():
                    list_of_age.append(line)
                print(list_of_age)

            remove_none = []
            for age in list_of_age:
                replace_age = age.replace("None", "19")
                remove_none.append(replace_age)
            print(list_of_age)
            webbrowser.open_new_tab('page5.html')
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
        file = open('page5.html', 'w')
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
        file.close()
        webbrowser.open_new_tab('page5.html')
    return web_page()


# Close the main function.
if __name__ == '__main__':
    main()