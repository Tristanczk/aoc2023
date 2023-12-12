from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, count, groupby, permutations, product
import math
import re
from sortedcontainers import SortedDict, SortedList, SortedDict
from collections import Counter
import argparse
import numpy as np
import functools

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

# recursive unoptimized solution (works for part 1) 
@functools.lru_cache(maxsize = None)
def dfs1(origin, cur, target):
	if len(cur) == len(origin):
		cur_nb = 0
		res = ""
		for c in cur:
			if c == "#":
				cur_nb += 1
			else:
				if cur_nb != 0:
					res += str(cur_nb) + ','
					cur_nb = 0
		if cur_nb != 0:
			res += str(cur_nb) + ','
		return res[:-1] == target
	else:
		n = len(cur)
		if origin[n] == '.':
			return dfs1(origin, cur + '.', target)
		elif origin[n] == '#':
			return dfs1(origin, cur + '#', target)
		else:
			return dfs1(origin, cur + '.', target) + dfs1(origin, cur + '#', target)

# recursive solution
def dfs2(memoization, origin, target, pos, current_broken_nb, count_broken):
	key = (pos, current_broken_nb, count_broken)
	if key in memoization:
		return memoization[key]
	if pos == len(origin):
		ret = 1 if count_broken == len(target) else 0
	elif count_broken > len(target) or (count_broken < len(target) and current_broken_nb > target[count_broken]):
		ret = 0
	elif origin[pos] == '#':
		ret = dfs2(memoization, origin, target, pos + 1, current_broken_nb + 1, count_broken)
	elif origin[pos] == '.':
		if current_broken_nb == 0:
			ret = dfs2(memoization, origin, target, pos + 1, 0, count_broken)
		else:
			if count_broken < len(target) and current_broken_nb == target[count_broken]:
				ret = dfs2(memoization, origin, target, pos + 1, 0, count_broken + 1)
			else:
				ret = 0
	else:
		broken_count = dfs2(memoization, origin, target, pos + 1, current_broken_nb + 1, count_broken)
		working_count = 0
		if current_broken_nb == 0:
			working_count = dfs2(memoization, origin, target, pos + 1, 0, count_broken)
		else:
			if count_broken < len(target) and current_broken_nb == target[count_broken]:
				working_count = dfs2(memoization, origin, target, pos + 1, 0, count_broken + 1)
			else:
				working_count = 0
		ret = broken_count + working_count
	memoization[key] = ret
	return ret

# dynamic programming solution
# dp[pos][cur_broken][broken_group]
# si springs[pos] == "#"
# dp(pos + 1, cur_broken + 1, broken_group + cur_broken == 0) += dp(pos, cur_broken, broken_group)

# si springs[pos] == '.'
# 	si cur_broken == 0 or cur_broken == values[broken_group]:
# 		dp(pos + 1, 0, broken_group) += dp(pos, cur_broken, broken_group)
def dp(springs, values):
	n = len(springs)
	m = len(values)
	dp = [[[0] * (m + 2) for i in range(n + 2)] for j in range(n + 1)]
	dp[0][0][0] = 1
	for i in range(n):
		for j in range(n + 1):
			for k in range(m + 1):
				cur = dp[i][j][k]
				if not cur:
					continue
				# handle if the character is a # or a ? and we suppose it is a #
				if springs[i] == '#' or springs[i] == '?':
					dp[i + 1][j + 1][k + (j == 0)] += cur
				# handle if the character is a . or a ? and we suppose it is a .
				if springs[i] == '.' or springs[i] == '?':
					if j == 0 or (j == values[k - 1]):
						dp[i + 1][0][k] += cur
	return dp[n][0][m]


# putting an additional '.' at the end of the line guarantees that we will always end up on a '.', and that we take into consideration the last block of "#"
def f1(s):
	l = s.split('\n')
	res = 0
	for line in l:
		springs, values = line.split()
		values = lrint(values)
		res += dp(springs + '.', values)
	return res

def f2(s):
	l = s.split('\n')
	res = 0
	for line in l:
		springs, values = line.split()
		new_springs, new_vals = "", ""
		for j in range(5):
			new_springs += springs
			new_vals += values
			if j != 4:
				new_springs += '?'
				new_vals += ','
		new_vals = lrint(new_vals)
		res += dp(new_springs + '.', new_vals)
	return res

args = parse_arguments()

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=12, year=2023).strip()
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
		__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=12, year=2023)
