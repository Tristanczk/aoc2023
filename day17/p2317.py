from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, count, groupby, permutations, product
import math
import re
from sortedcontainers import SortedDict, SortedList, SortedDict
from collections import Counter
import argparse
import numpy as np
import heapq
import sys

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
	h, w = len(l), len(l[0])
	memo = {}
	queue = [(0,0,(0,0),0,0)]
	while queue:
		r, c, di, cur_dir, cur_val = heapq.heappop(queue)
		key = (r, c, di, cur_dir)
		if (r, c, di, cur_dir) in memo:
			if cur_val >= memo[key]:
				continue
		memo[key] = cur_val
		for d in direction_4:
			dh, dw = d
			new_r, new_c = r + dh, c + dw
			new_cur_dir = 1 if d != di else cur_dir + 1
			if dh == -di[0] and dw == -di[1]:
				continue
			elif new_r < 0 or new_r >= h or new_c < 0 or new_c >= w:
				continue
			elif new_cur_dir > 3:
				continue
			else:
				increase = int(l[new_r][new_c])
				heapq.heappush(queue, (new_r, new_c, d, new_cur_dir, cur_val + increase))
	ans = float('inf')
	for (r,c,_,__), v in memo.items():
		if r == h - 1 and c == w - 1:
			ans = min(ans, v)
	return ans

def f2(s):
	l = s.split('\n')
	h, w = len(l), len(l[0])
	memo = {}
	queue = [(0,0,(0,0),0,0)]
	while queue:
		r, c, di, cur_dir, cur_val = heapq.heappop(queue)
		key = (r, c, di, cur_dir)
		if (r, c, di, cur_dir) in memo:
			if cur_val >= memo[key]:
				continue
		memo[key] = cur_val
		for d in direction_4:
			dh, dw = d
			new_r, new_c = r + dh, c + dw
			new_cur_dir = 1 if d != di else cur_dir + 1
			if dh == -di[0] and dw == -di[1]:
				continue
			elif new_r < 0 or new_r >= h or new_c < 0 or new_c >= w:
				continue
			elif new_cur_dir > 10:
				continue
			if d != di and cur_dir != 0 and cur_dir < 4:
				continue
			else:
				increase = int(l[new_r][new_c])
				heapq.heappush(queue, (new_r, new_c, d, new_cur_dir, cur_val + increase))
	ans = float('inf')
	for (r,c,_,cur_dir), v in memo.items():
		if r == h - 1 and c == w - 1 and cur_dir >= 4:
			ans = min(ans, v)
	return ans

args = parse_arguments()

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=17, year=2023).strip()
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
		__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=17, year=2023)
