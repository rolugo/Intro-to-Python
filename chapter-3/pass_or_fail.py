# Get a test score.
score = int(input('Enter your test score: '))

# Did the user pass?
if score > 59:
    print('Congratulations!')
    print('You passed the exam.')
else:
    print('Sorry, you did not pass the exam.')
    print('Study, and then try again.')