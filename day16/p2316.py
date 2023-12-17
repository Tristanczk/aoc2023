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

def bfs(start, l):
	h, w = len(l), len(l[0])
	energized = set()
	seen = set()
	lights = deque([start])
	while lights:
		pos, dir = lights.popleft()
		r, c = pos
		if (pos, dir) in seen:
			continue
		seen.add((pos, dir))
		energized.add(pos)
		dh, dw = dir
		new_pos = (r+dh, c+dw)
		r, c = new_pos
		if r < 0 or r >= h or c < 0 or c >= w:
			continue
		if l[r][c] == '.':
			lights.append([new_pos, dir])
		elif l[r][c] == '/':
			new_dir = (-dw, -dh)
			lights.append([new_pos, new_dir])
		elif l[r][c] == '\\':
			new_dir = (dw, dh)
			lights.append([new_pos, new_dir])
		elif l[r][c] == '-':
			if dh == 0:
				lights.append([new_pos, dir])
			else:
				lights.append([new_pos, (0, -1)])
				lights.append([new_pos, (0, 1)])
		else:
			if dw == 0:
				lights.append([new_pos, dir])
			else:
				lights.append([new_pos, (1, 0)])
				lights.append([new_pos, (-1, 0)])
		# print(lights)
	# mat = [['.'] * w for i in range(h)]
	# for r, c in energized:
	# 	mat[r][c] = "#"
	# print(mat)
	return len(energized) - 1


def f1(s):
	l = s.split('\n')
	h, w = len(l), len(l[0])
	energized = set()
	seen = set()
	lights = deque([[(0, -1), (0, 1)]])
	while lights:
		pos, dir = lights.popleft()
		r, c = pos
		if (pos, dir) in seen:
			continue
		seen.add((pos, dir))
		energized.add(pos)
		dh, dw = dir
		new_pos = (r+dh, c+dw)
		r, c = new_pos
		if r < 0 or r >= h or c < 0 or c >= w:
			continue
		if l[r][c] == '.':
			lights.append([new_pos, dir])
		elif l[r][c] == '/':
			new_dir = (-dw, -dh)
			lights.append([new_pos, new_dir])
		elif l[r][c] == '\\':
			new_dir = (dw, dh)
			lights.append([new_pos, new_dir])
		elif l[r][c] == '-':
			if dh == 0:
				lights.append([new_pos, dir])
			else:
				lights.append([new_pos, (0, -1)])
				lights.append([new_pos, (0, 1)])
		else:
			if dw == 0:
				lights.append([new_pos, dir])
			else:
				lights.append([new_pos, (1, 0)])
				lights.append([new_pos, (-1, 0)])
		# print(lights)
	# mat = [['.'] * w for i in range(h)]
	# for r, c in energized:
	# 	mat[r][c] = "#"
	# print(mat)
	return len(energized) - 1

def f2(s):
	l = s.split('\n')
	h, w = len(l), len(l[0])
	res = 0
	for i in range(h):
		res = max(res, bfs([(i, -1), (0,1)], l))
		res = max(res, bfs([(i, w), (0,-1)], l))
	for j in range(w):
		res = max(res, bfs([(-1, j), (1,0)], l))
		res = max(res, bfs([(h, j), (-1,0)], l))
	return res

args = parse_arguments()

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=16, year=2023).strip()
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

# if args.v:
# 	part = input("Submit? (a/b) | ")
# 	if part == "a" or part == "b":
# 		__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=16, year=2023)
