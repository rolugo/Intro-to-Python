# Rosendo Lugo Jr.
# Chapter 6 Programming
# Personal Web Page Generator
import os
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
            filepath = 'page5.html'
            path = os.listdir(filepath)
            for content in path:
                    print(content)
            current = f'{age}'
            default_age = 21
            total = 0
            for content in path:
                counter = 0
                with open(page5.html + content, 'r', encoding='utf-8') as file:
                    result = file.read()
                    counter = result.count(current)
                result = result.replace(current, default_age)
                with open(page5.html + content, 'w', encoding='utf-8') as page_temp.html:
                    page_temp.html.write(result)
                if counter:
                     print(counter, ':', counter, 'changes')
                    total +=1
            print("totally", total, 'files changed')


            #with open('page5.html', 'r') as file:
                #with open('page_temp.html', 'w') as file2:
                    #for line in file:
                        #file2.write(line)

                #file.write('Test')
                #file.seek(0)
                #file.write('R')
                #size_to_read = 10
                #file_contents = file.read(size_to_read)
                #print(file_contents, end='')

                #file.seek(0)
                #file_contents = file.read(size_to_read)
                #print(file_contents)
                #print(file.tell())

                #while len(file_contents) > 0:
                    #print(file_contents, end='*')
                    #file_contents = file.read(size_to_read)
                #file_contents = file.readline()
                #print(file_contents)

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
        file.write(f'I am {age} years old.\n')   # Add the age
        file.write("<p/>\n")                    # Close the paragraph tag
        file.write("<p>\n")                     # Open the paragraph tag
        file.write(" " + description + "\n")    # Add the description
        file.write("<p/>\n")                    # Close the paragraph tag
        file.write("</body>\n")                 # Close the body
        file.write("</html>\n")                 # End html
        file.close()
        #webbrowser.open_new_tab("page7.html")
    return web_page()


# Close the main function.
if __name__ == '__main__':
    main()