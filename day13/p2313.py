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

def check_equal_column(mat, col1, col2):
	n = len(mat)
	count = 0
	print(col1, col2)
	for k in range(n):
		if mat[k][col1] == mat[k][col2]:
			count += 1
		else:
			break
	return count == n

def check_equal_column_error(mat, col1, col2):
	n = len(mat)
	count = 0
	for k in range(n):
		if mat[k][col1] != mat[k][col2]:
			count += 1
	return count


def f1(s):
	l = s.split('\n\n')
	res = 0
	for block in l:
		line = block.split("\n")
		n, m = len(line), len(line[0])
		cur = -1
		for i in range(n - 1):
			count = 0
			check = min(i + 1, n - i - 1)
			for k in range(check):
				if line[i - k] == line[i + 1 + k]:
					count += 1
			if count == check:
				cur = 100 * (i + 1)
				break
		if cur != -1:
			res += cur
			continue
		for j in range(m - 1):
			count = 0
			check = min(j + 1, m - j - 1)
			for k in range(check):
				if check_equal_column(line, j - k, j + 1 + k):
					count += 1
			if count == check:
				cur = j + 1
				break
		res += cur
	return res

def f2(s):
	l = s.split('\n\n')
	res = 0
	for block in l:
		line = block.split("\n")
		n, m = len(line), len(line[0])
		cur = 0
		count_reflect = 0
		for i in range(n - 1):
			error = 0
			check = min(i + 1, n - i - 1)
			for k in range(check):
				error += len([x for x in range(m) if line[i - k][x] != line[i + 1 + k][x]])
			if error == 1:
				cur = 100 * (i + 1)
				break
		if cur != 0:
			res += cur
			continue
		for j in range(m - 1):
			check = min(j + 1, m - j - 1)
			error = 0
			for k in range(check):
				error += check_equal_column_error(line, j - k, j + 1 + k) 
			if error == 1:
				cur = j + 1
				break
		res += cur
	return res

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
