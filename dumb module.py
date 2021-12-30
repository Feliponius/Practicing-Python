anyNum = int(input("please input any number. "))

divByFour = anyNum % 4
oddOrEven = anyNum % 2

if divByFour == 0:
    print('Wow...You\'re big on quarter\'s aint\'cha?')
elif oddOrEven >= 1:
    print('You sure are an odd one!')
else:
    print('Getting even with me for all these puns?')

print("Great! Now let's get two more numbers and see if they divide odd or evenly.")
num = int(input("First number to be divided: "))
check = int(input("Next number to divide into the first number: "))

divMath = num % check

if divMath >= 1:
    print("Odd! Isn't that intersting!")
else:
    print("Even! That was fun!")




