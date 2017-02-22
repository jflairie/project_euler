"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import pandas as pd


def collatz(x):
    """
    Function that applies the Collatz logic on integer x
    """
    if x % 2 == 0:
        return x / 2
    else:
        return 3 * x + 1


def boucle(x):
    """
    Function that computes the length of a Collatz chain
    """
    counter = 1
    y = collatz(x)
    while y != 1:
        y = collatz(y)
        counter += 1
    return counter


def main():
    df = pd.DataFrame(data=range(1, 1000000), columns={'integer_start'})
    df['counter'] = df.apply(lambda row: boucle(row['integer_start']), axis=1)
    result = df[df['counter'] == df['counter'].max()]['integer_start'].item()
    print "Result is", result


if __name__ == '__main__':
    main()
