# This program gets three names from the user
# and writes them to a file.

def main():

    # Open a file named friends.txt.
    myfile = open('friends.txt', 'a')

    # Append additional data to it's existing file.
    myfile.write('Matt\n')
    myfile.write('Chris\n')
    myfile.write('Suze\n')

    # Close the file.
    myfile.close()
    print('The names were written to friends.txt.')

# Call the main function.
if __name__ == '__main__':
    main()

