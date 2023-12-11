from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, count, groupby, permutations, product
import math
import re
from sortedcontainers import SortedDict, SortedList, SortedDict
from collections import Counter
import argparse
import numpy as np
import bisect

direction_4 = [(0,1), (0,-1), (1,0), (-1,0)]
direction_8 = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]

def count_list_elem(l, r, listy):
	lower_index = bisect.bisect_left(listy, l)
	upper_index = bisect.bisect_right(listy, r)
	return upper_index - lower_index


def parse_arguments():
	parser = argparse.ArgumentParser(prog="aoc",
									description="solution for an aoc day")
	parser.add_argument('-v', action='store_true', help="validate")
	parser.add_argument('-p', action='store_true', help="second part")
	args = parser.parse_args()
	return args

rint = lambda x: map(int, re.findall(r"\d+", x))
lrint = lambda x: list(map(int, re.findall(r"\d+", x)))

def f1(s):
	l = s.split('\n')
	mat = [list(x) for x in l]
	h,w = len(mat), len(mat[0])
	new_col = []
	new_line = []
	pos = []
	for j in range(w):
		c = 0
		for i in range(h):
			if mat[i][j] == '#':
				pos.append((i, j))
			else:
				c += 1
		if c == h:
			new_col.append(j)
	for i in range(h):
		if mat[i].count("#") == 0:
			new_line.append(i)
	res = 0
	nb = 0
	for i in range(len(pos) - 1):
		for j in range(i + 1, len(pos)):
			ra, ca = pos[i]
			rb, cb = pos[j]
			ra, rb = min(ra, rb), max(ra, rb)
			ca, cb = min(ca, cb), max(ca, cb)
			dr, dc = rb - ra, cb - ca
			dr += count_list_elem(ra, rb, new_line)
			dc += count_list_elem(ca, cb, new_col)
			res += dr + dc
			nb += 1
	return res


def f2(s):
	l = s.split('\n')
	mat = [list(x) for x in l]
	h,w = len(mat), len(mat[0])
	new_col = []
	new_line = []
	pos = []
	for j in range(w):
		c = 0
		for i in range(h):
			if mat[i][j] == '#':
				pos.append((i, j))
			else:
				c += 1
		if c == h:
			new_col.append(j)
	for i in range(h):
		if mat[i].count("#") == 0:
			new_line.append(i)
	res = 0
	nb = 0
	for i in range(len(pos) - 1):
		for j in range(i + 1, len(pos)):
			ra, ca = pos[i]
			rb, cb = pos[j]
			ra, rb = min(ra, rb), max(ra, rb)
			ca, cb = min(ca, cb), max(ca, cb)
			dr, dc = rb - ra, cb - ca
			dr += count_list_elem(ra, rb, new_line) * 999999
			dc += count_list_elem(ca, cb, new_col) * 999999
			res += dr + dc
			nb += 1
	return res

args = parse_arguments()

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=11, year=2023).strip()
	open("in", "w").write(indata)

if not args.p:
	if exdata:
		print("ex1:", f1(exdata))
	if args.v:
		print("in1:", (in1 := f1(indata)))
else:
	if exdata:
		print("ex2:", f2(exdata))
	if args.v:
		print("in2:", (in2 := f2(indata)))

if args.v:
	part = input("Submit? (a/b) | ")
	if part == "a" or part == "b":
		__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=11, year=2023)
