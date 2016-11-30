my_input = input("Please enter number")


for n in range (1, my_input):
    if n % 3==0 and n % 5==0:
        print "Fizzbuzz"
    elif n % 3==0:
        print "Fizz"
    elif n % 5==0:
        print "Buzz"
    else:
        print n