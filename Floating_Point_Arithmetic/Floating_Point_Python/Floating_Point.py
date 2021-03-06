##################################################################
# Resolving the issue of floating point arithmetic 
# Links explaining the issue: 
# https://docs.python.org/3/tutorial/floatingpoint.html
# https://docs.python.org/3/library/decimal.html
# https://www.geeksforgeeks.org/floating-point-error-in-python/

# Usage of <round()> or <.format(args,'.f')>
# is not the best solution as it is up for human intuition
# which is extremely prone to errors 

# Code written by yuyusio
##################################################################

from decimal import *
# Enable ANSI Escape Code in Windows Terminal
import os
os.system("")


def floatify(num):
    pos = 0

    while num[pos] != '.':
        pos += 1

    return (num[:pos],num[pos+1:])

def add_float(num1, num2):
    num1 = floatify(num1)
    num2 = floatify(num2)

    num_front = int(num1[0]) + int(num2[0])
    num_front = str(num_front)

    if len(num1[1]) > len(num2[1]):
        dif = len(num1[1])-len(num2[1])
        num_back = int(num1[1]) + int(num2[1]) * (10**(dif))
        num_back = str(num_back)
        if len(num_back) > len(num1[1]):
            num_front = str(int(num_front)+1)
            num_back = num_back[1:]

    elif len(num2[1]) > len(num1[1]):
        dif = len(num2[1])-len(num1[1])
        num_back = int(num2[1]) + int(num1[1]) * (10**(dif))
        num_back = str(num_back)
        if len(num_back) > num2[1]:
            num_front = str(int(num_front)+1)
            num_back = num_back[1:]

    else:
        num_back = int(num2[1]) + int(num1[1])
        num_back = str(num_back)
        if len(num_back) > len(num1[1]):
            num_front = str(int(num_front)+1)
            num_back = num_back[1:]

    return num_front + '.' + num_back


def dif_float(num1, num2):
    num1 = floatify(num1)
    num2 = floatify(num2)

    num_front = int(num1[0]) - int(num2[0])

    if len(num1[1]) > len(num2[1]):
        num_back_len = len(num1[1])
        dif = len(num1[1])-len(num2[1])
        num_back = int(num1[1]) - int(num2[1]) * (10**(dif))

    elif len(num2[1]) > len(num1[1]):
        num_back_len = len(num2[1])
        dif = len(num2[1])-len(num1[1])
        num_back = int(num1[1]) * (10**(dif)) - int(num2[1])

    else:
        num_back_len = len(num1[1])
        num_back = int(num1[1]) - int(num2[1])

    if num_back < 0:
        num_front -= 1
        num_back = 10**num_back_len+num_back

    if len(str(num_back)) < num_back_len:
        num_back = '0'*(num_back_len-len(str(num_back))) + str(num_back)

    return str(num_front) + '.' + str(num_back)


if __name__ == "__main__":

    print('\033[30m'+'-'*100+'\033[0m')

    print('\033[31m'+"Precision of Normal python arithmetic operation: "+str(getcontext().prec)+'\033[0m')

    print('\033[30m'+'-'*100+'\033[0m')

    a = 0.1
    b = 0.2

    print('\033[31m'+"Normal python arithmetic operation: "+'\033[0m')
    print(a+b)
    print(Decimal(a+b))
    print('')
    print('\033[34m'+"Modified arithmetic operation: "+'\033[0m')
    print(add_float("0.1","0.2"))

    print('\033[30m'+'-'*100+'\033[0m')

    a = 4782.9681
    b = 1920823.4

    print('\033[31m'+"Normal python arithmetic operation result: "+'\033[0m')
    print(a+b)
    print(Decimal(a+b))
    print('')
    print('\033[34m'+"Modified arithmetic operation result: "+'\033[0m')
    print(add_float("4782.9681","1920823.4"))

    print('\033[30m'+'-'*100+'\033[0m')

    a = 2.0
    b = 1.8

    print('\033[31m'+"Normal python arithmetic operation result: "+'\033[0m')
    print(a-b)
    print(Decimal(a-b))
    print('')
    print('\033[34m'+"Modified arithmetic operation result: "+'\033[0m')
    print(dif_float("2.0","1.8"))

    print('\033[30m'+'-'*100+'\033[0m')