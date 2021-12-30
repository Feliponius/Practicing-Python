# Get a number from the user
anyNum = int(input("please input any number. "))

# Set two variables specifically for checking if divisible by four or otherwise if it's even/odd
divByFour = anyNum % 4
oddOrEven = anyNum % 2

# Algorithm to check if by four, or odd/even.
if divByFour == 0:
    print('Wow...You\'re big on quarter\'s aint\'cha?')
elif oddOrEven >= 1:
    print('You sure are an odd one!')
else:
    print('Getting even with me for all these puns?')

# Second input to have user check if two separate numbers are odd or even.

print("Great! Now let's get two more numbers and see if they divide odd or evenly.")
num = int(input("First number to be divided: "))
check = int(input("Next number to divide into the first number: "))

divMath = num % check

if divMath >= 1:
    print("Odd! Isn't that intersting!")
else:
    print("Even! That was fun!")




