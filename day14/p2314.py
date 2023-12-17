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

def calculate_val_col(mat, c):
	h = len(mat)
	res = 0
	cur = h
	for i in range(h):
		if mat[i][c] == 'O':
			res += cur
			cur -= 1
		elif mat[i][c] == '#':
			cur = h - i - 1
	return res

def calculate_cycle(mat):
	h, w = len(mat), len(mat[0])
	#north
	for j in range(w):
		cur = 0
		for i in range(h):
			if mat[i][j] == 'O':
				mat[i][j] = '.'
				mat[cur][j] = 'O'
				cur += 1
			elif mat[i][j] == '#':
				cur = i + 1
	# west
	for i in range(h):
		cur = 0
		for j in range(w):
			if mat[i][j] == 'O':
				mat[i][j] = '.'
				mat[i][cur] = 'O'
				cur += 1
			elif mat[i][j] == '#':
				cur = j + 1
	# south
	for j in range(w):
		cur = h - 1
		for i in range(h - 1, -1, -1):
			if mat[i][j] == 'O':
				mat[i][j] = '.'
				mat[cur][j] = 'O'
				cur -= 1
			elif mat[i][j] == '#':
				cur = i - 1
	# east
	for i in range(h):
		cur = w - 1
		for j in range(w - 1, -1, -1):
			if mat[i][j] == 'O':
				mat[i][j] = '.'
				mat[i][cur] = 'O'
				cur -= 1
			elif mat[i][j] == '#':
				cur = j - 1
	
	return mat

def calc_load(mat):
	h, w = len(mat), len(mat[0])
	res = 0
	for i in range(h):
		res += len([k for k in mat[i] if k == 'O']) * (h - i)
	return res
		

def f1(s):
	l = s.split('\n')
	h, w = len(l), len(l[0])
	res = 0
	for j in range(w):
		res += calculate_val_col(l, j)
	return res

def f2(s):
	l = s.split('\n')
	l = [list(x) for x in l]
	seen = {}
	countdown = -1
	i = 1
	# printed the output and found the cycle manually
	# cycle started at iteration 83 and was 42 ieration long : 1000000000 - 82 % 42 = 36
	# answer is 36th value of cycle
	while countdown != 0:
		l = calculate_cycle(l)
		a = calc_load(l)
		if countdown != -1:
			countdown -= 1
		elif a in seen:
			countdown = 2 * len(seen)
		else:
			seen.add(a)
		print(a)
		i += 1
	return len(seen)

args = parse_arguments()

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=14, year=2023).strip()
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
		__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=14, year=2023)
