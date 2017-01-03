# A Pythagorean triplet is a set of 3 natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in xrange(1, 333, 1):
    for b in xrange(a + 1, 500, 1):
        for c in xrange(b + 1, 500, 1):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print a * b * c
