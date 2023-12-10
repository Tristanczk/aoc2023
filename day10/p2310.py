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

def f1(s):
	l = s.split('\n')
	n, m = len(l), len(l[0])
	start = ()
	for i in range(n):
		for j in range(m):
			if l[i][j] == 'S':
				start = (i, j)
				break
	r, c = start
	start_dir = []
	if r - 1 >= 0 and (l[r - 1][c] == '|' or l[r - 1][c] == '7' or l[r - 1][c] == 'F'):
		start_dir.append((-1, 0))
	if r + 1 < n and (l[r + 1][c] == '|' or l[r + 1][c] == 'L' or l[r + 1][c] == 'J'):
		start_dir.append((1, 0))
	if c - 1 >= 0 and (l[r][c - 1] == '-' or l[r][c - 1] == 'F' or l[r][c - 1] == 'L'):
		start_dir.append((0, -1))
	if c + 1 < m and (l[r][c + 1] == '-' or l[r][c + 1] == '7' or l[r][c + 1] == 'J'):
		start_dir.append((0, 1))
	start_direct = start_dir[0]
	prev_r, prev_c = start
	r, c = r + start_direct[0], c + start_direct[1]
	step = 1
	while ((r, c) != start):
		step += 1
		if l[r][c] == '|':
			if prev_r == r - 1:
				prev_r = r
				r = r + 1
			else:
				prev_r = r
				r = r - 1
		elif l[r][c] == '-':
			if prev_c == c - 1:
				prev_c = c
				c += 1
			else:
				prev_c = c
				c -= 1
		elif l[r][c] == 'F':
			if prev_c == c + 1:
				prev_c = c
				r += 1
			else:
				prev_r = r
				c += 1
		elif l[r][c] == 'L':
			if prev_c == c + 1:
				prev_c = c
				r -= 1
			else:
				prev_r = r
				c += 1
		elif l[r][c] == '7':
			if prev_c == c - 1:
				prev_c = c
				r += 1
			else:
				prev_r = r
				c -= 1
		elif l[r][c] == 'J':
			if prev_c == c - 1:
				prev_c = c
				r -= 1
			else:
				prev_r = r
				c -= 1
	return step // 2

def f2(s):
	l = s.split('\n')
	n, m = len(l), len(l[0])
	mat = [list(l[i]) for i in range(n)]
	start = ()
	for i in range(n):
		for j in range(m):
			if l[i][j] == 'S':
				start = (i, j)
				break
	r, c = start
	start_dir = []
	if r - 1 >= 0 and (l[r - 1][c] == '|' or l[r - 1][c] == '7' or l[r - 1][c] == 'F'):
		start_dir.append((-1, 0))
	if r + 1 < n and (l[r + 1][c] == '|' or l[r + 1][c] == 'L' or l[r + 1][c] == 'J'):
		start_dir.append((1, 0))
	if c - 1 >= 0 and (l[r][c - 1] == '-' or l[r][c - 1] == 'F' or l[r][c - 1] == 'L'):
		start_dir.append((0, -1))
	if c + 1 < m and (l[r][c + 1] == '-' or l[r][c + 1] == '7' or l[r][c + 1] == 'J'):
		start_dir.append((0, 1))
	start_direct = start_dir[0]
	prev_r, prev_c = start
	mat[r][c] = 'X'
	r, c = r + start_direct[0], c + start_direct[1]
	step = 1
	while ((r, c) != start):
		mat[r][c] = 'X'
		if l[r][c] == '|':
			if prev_r == r - 1:
				prev_r = r
				r = r + 1
			else:
				prev_r = r
				r = r - 1
		elif l[r][c] == '-':
			if prev_c == c - 1:
				prev_c = c
				c += 1
			else:
				prev_c = c
				c -= 1
		elif l[r][c] == 'F':
			if prev_c == c + 1:
				prev_c = c
				r += 1
			else:
				prev_r = r
				c += 1
		elif l[r][c] == 'L':
			if prev_c == c + 1:
				prev_c = c
				r -= 1
			else:
				prev_r = r
				c += 1
		elif l[r][c] == '7':
			if prev_c == c - 1:
				prev_c = c
				r += 1
			else:
				prev_r = r
				c -= 1
		elif l[r][c] == 'J':
			if prev_c == c - 1:
				prev_c = c
				r -= 1
			else:
				prev_r = r
				c -= 1
	count = 0
	if start_dir[0] in [(0,1), (0,-1)] and start_dir[1] in [(0,1), (0,-1)]:
		check = 0
	else:
		check = 1
	for k in range(n):
		inside = False
		for w in range(m):
			if mat[k][w] == 'X':
				# note the starting position of my input is a 7 so no need to consider it
				if l[k][w] in "|JL":
					inside = not inside
			else:
				count += inside
	return count

args = parse_arguments()

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=10, year=2023).strip()
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
		__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=10, year=2023)
