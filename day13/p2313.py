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

def transpose(mat):
	return list(map(list, zip(*mat)))

def solve(s, error_accepted):
	def solve_horizontal(mat, error_accepted):
		h, w = len(mat), len(mat[0])
		for i in range(h - 1):
			error = 0
			check = min(i + 1, h - i - 1)
			for j in range(check):
				error += len([k for k in range(w) if mat[i - j][k] != mat[i + 1 + j][k]])
			if error == error_accepted:
				return i + 1
		return None
	l = s.split('\n\n')
	res = 0
	for block in l:
		line = [list(x) for x in block.split("\n")]
		row = solve_horizontal(line, error_accepted)
		if row is not None:
			res += row * 100
		else:
			res += solve_horizontal(transpose(line), error_accepted)
	return res

def f1(s):
	return solve(s, 0)

def f2(s):
	return solve(s, 1)

args = parse_arguments()

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=13, year=2023).strip()
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
		__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=13, year=2023)
