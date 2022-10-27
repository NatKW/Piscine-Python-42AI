from sys import argv

"""
    Write a program that takes two integers A and B as arguments and prints the result of the following operations:
    Sum: A+B
    Difference: A-B Product: A*B
    Quotient: A/B Remainder: A%B
    Keep it simple!

"""
if (len(argv) == 1):
    print('Provide two arguments')
else:
    assert argv[1].isnumeric() == True, 'Provide only integers as arguments'
    assert argv[2].isnumeric() == True, 'Provide only integers as arguments'
    assert len(argv) == 3, 'Too many arguments'
    S = int(argv[1]) + int(argv[2])
    D = int(argv[1]) - int(argv[2])
    P = int(argv[1]) * int(argv[2])
    print("Sum: ", S,"\nDifference: ", D,"\nProduct: ", P)
    if int(argv[1]) == 0 or int(argv[2]) == 0:
        print("Quotient: ERROR(div by zero)", "\nRemainder: ERROR(modulo by zero)")
    else:
        print("Quotient: ", (int(argv[1]) / int(argv[2])))
        print("Remainder: ", (int(argv[1]) % int(argv[2])))
        

