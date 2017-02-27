"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def sum_of_digits(number):
    result = 0
    for i in str(number):
        result += int(i)
    return result


def main():
    print "Number to raise to power: "
    number = int(raw_input('> '))
    print("Power: ")
    power = int(raw_input('> '))
    print "The sum of the digits of the number {0}^{1} is {2}.\
    ".format(number, power, sum_of_digits(number**power))


if __name__ == '__main__':
    main()
