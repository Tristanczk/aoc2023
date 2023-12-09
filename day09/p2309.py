from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, count, groupby, permutations, product
import math
import re
from sortedcontainers import SortedDict, SortedList, SortedDict
from collections import Counter

direction_4 = [(0,1), (0,-1), (1,0), (-1,0)]
direction_8 = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]

rint = lambda x: map(int, re.findall(r"\d+", x))
lrint = lambda x: list(map(int, re.findall(r"\d+", x)))

def f1(s):
	l = s.split("\n")
	res = 0
	for line in l:
		line = [int(x) for x in line.split()]
		d = [line]
		cur = line[-1]
		while True:
			diff = []
			n = len(d[-1])
			for i in range(1, n):
				diff.append(d[-1][i] - d[-1][i - 1])
			cur += diff[-1]
			if all(v == 0 for v in diff):
				break
			d.append(diff)
		res += cur
	return res

def f2(s):
	l = s.split("\n")
	res = 0
	for line in l:
		line = [int(x) for x in line.split()]
		d = [line]
		cur = line[-1]
		while True:
			diff = []
			n = len(d[-1])
			for i in range(1, n):
				diff.append(d[-1][i] - d[-1][i - 1])
			if all(v == 0 for v in diff):
				break
			d.append(diff)
		cur = 0
		for j in range(len(d) - 1, -1, -1):
			cur = d[j][0] - cur
		res += cur
	return res

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=9, year=2023).strip()
	open("in", "w").write(indata)

# if exdata:
# 	print("ex1:", f1(exdata))
# print("in1:", (in1 := f1(indata)))
if exdata:
	print("ex2:", f2(exdata))
print("in2:", (in2 := f2(indata)))

part = input("Submit? (a/b) | ")
if part == "a" or part == "b":
	__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=9, year=2023)
