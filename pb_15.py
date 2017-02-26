# -*- coding: utf-8 -*
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
"""
Problem complextity can be simplified to finding how many arrangementare possible
with 20 'R's and 20 'D's. "20 parmi 40" 40! / (40-20)!20!
"""
from math import factorial as f

print "What is the size of the grid (heigth or width)?"
grid_size = int(raw_input('> '))

routes = f(grid_size * 2) / (f(grid_size) * f(grid_size))

print "There are {0} routes possible in a {1}x{1} grid\
.".format(routes, grid_size)
