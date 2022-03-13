def collatz(number):
    if (number % 2) == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    return result

print('Please enter a number:')

try:
    enter = int(input())
except ValueError:
    print('That\'s not a number, try again:')
    enter = int(input())

if enter > 0:
    while enter != 1:
        enter = collatz(enter)
        print(enter)
else:
    print('Number must be positive or else everything breaks. Try again:')
    try:
        enter = int(input())
    except ValueError:
        print('That\'s not a number, try again:')
        enter = int(input())
    while enter != 1:
        enter = collatz(enter)
        print(enter)



