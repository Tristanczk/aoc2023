from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, count, groupby, permutations, product
import math
import re
from sortedcontainers import SortedDict, SortedList, SortedDict
from collections import Counter
import argparse
import numpy as np

direction_4 = [(0,1), (0,-1), (1,0), (-1,0)]
direction_8 = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]

def parse_arguments():
	parser = argparse.ArgumentParser(prog="aoc",
									description="solution for an aoc day")
	parser.add_argument('-v', action='store_true', help="validate")
	parser.add_argument('-p', action='store_true', help="second part")
	args = parser.parse_args()
	return args

rint = lambda x: map(int, re.findall(r"\d+", x))
lrint = lambda x: list(map(int, re.findall(r"\d+", x)))

# shoelace formula calculates the area (times 2) of the polygon shoelace(r,c) = 2*A
def shoelace_formula(r, c):
	n = len(r)
	res = 0
	for i in range(n - 1):
		res += (c[i] * r[i + 1] - c[i + 1] * r[i])
	return abs(res)

def f1(s):
	l = s.split('\n')
	direc = {'R': 0, 'L': 1, 'D':2, 'U':3}
	cur = [0, 0]
	r = []
	c = []
	r.append(cur[0])
	c.append(cur[1])
	res = 0
	for line in l:
		dir_, len_, color = line.split()
		move = direction_4[direc[dir_]]
		dr, dc = move
		cur[0] += dr * int(len_)
		cur[1] += dc * int(len_)
		r.append(cur[0])
		c.append(cur[1])
		res += int(len_)
	r = [0, 0, 2, 2, 0]
	c = [0, 2, 2, 0, 0]
	# we use pick theorem, A is the area, i the number of interior point, b the number of boundary point
	# A = i + b/2 - 1 -> A + 1 = i + b / 2 -> i + b = A + b / 2 + 1 = shoelace(r,c) / 2 + b / 2 + 1
	res += shoelace_formula(r, c)
	return res // 2 + 1

# try with a matrix that isn't working
# def f1(s):
# 	l = s.split('\n')
# 	h, w = 2000, 2000
# 	mat = [['.'] * h for i in range(w)]
# 	mat[h//2][w//2] = '#'
# 	cur = [h//2, h//2]
# 	direc = {'R': 0, 'L': 1, 'D':2, 'U':3}
# 	for line in l:
# 		dir_, len_, color = line.split()
# 		move = direction_4[direc[dir_]]
# 		dr, dc = move
# 		for i in range(int(len_)):
# 			cur[0] += dr
# 			cur[1] += dc
# 			mat[cur[0]][cur[1]] = "#"
# 	res = 0
# 	for i in range(h):
# 		j = 0
# 		inside = False
# 		possible = 0
# 		while j < w:
# 			while j < w and mat[i][j] == '.':
# 				if inside: 
# 					possible += 1
# 				j += 1
# 			if j == w:
# 				break
# 			while j < w and mat[i][j] == '#':
# 				res += 1
# 				j += 1
# 			if inside:
# 				res += possible
# 				possible = 0
# 			inside = not inside
# 		# print(res)
# 	return res


def f2(s):
	l = s.split('\n')
	convert = ['R', 'D', 'L', 'U']
	direc = {'R': 0, 'L': 1, 'D':2, 'U':3}
	cur = [0, 0]
	r = []
	c = []
	r.append(cur[0])
	c.append(cur[1])
	res = 0
	for line in l:
		dir_, len_, color = line.split()
		dir_ = convert[int(color[-2])] 
		len_ = int(color[2:-2], 16)
		move = direction_4[direc[dir_]]
		dr, dc = move
		cur[0] += dr * len_
		cur[1] += dc * len_
		r.append(cur[0])
		c.append(cur[1])
		res += len_
	res += shoelace_formula(r, c)
	return res // 2 + 1

args = parse_arguments()

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=18, year=2023).strip()
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
		__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=18, year=2023)
