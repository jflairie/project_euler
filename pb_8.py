"""
The four adjacent digits in the 1000-digit number that have the greatest
product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
"""

figure = 731671765313306249192251196744265747423553491949349698352031277450632\
    62395783180169848018694788518438586156078911294949545950173795833195285320\
    88055111254069874715852386305071569329096329522744304355766896648950445244\
    52316173185640309871112172238311362229893423380308135336276614282806444486\
    64523874930358907296290491560440772390713810515859307960866701724271218839\
    98797908792274921901699720888093776657273330010533678812202354218097512545\
    40594752243525849077116705560136048395864467063244157221553975369781797784\
    61740649551492908625693219784686224828397224137565705605749026140797296865\
    24145351004748216637048440319989000889524345065854122758866688116427171479\
    92444292823086346567481391912316282458617866458359124566529476545682848912\
    88314260769004224219022671055626321111109370544217506941658960408071984038\
    50962455444362981230987879927244284909188845801561660979191338754992005240\
    63689912560717606058861164671094050775410022569831552000559357297257163626\
    9561882670428252483600823257530420752963450

figure = map(int, [i for i in str(figure)])

result = 0
biggest = 0
j = 13

for i in xrange(0, 1000 - j, 1):
    number = figure[i] * figure[i + 1] * figure[i + 2] * figure[i + 3]
    * figure[i + 4] * figure[i + 5] * figure[i + 6] * figure[i + 7]
    * figure[i + 8] * figure[i + 9] * figure[i + 10] * figure[i + 11]
    * figure[i + 12]

    if number > biggest:
        biggest = number
        index = i

print biggest, index

figure[index:index + 13]
