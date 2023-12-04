from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, count, groupby, permutations, product
import math
import re
from sortedcontainers import SortedDict, SortedList, SortedDict
from collections import Counter

direction_4 = [(0,1), (0,-1), (1,0), (-1,0)]
direction_8 = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]

rint = lambda x: map(int, re.findall(r"\d+", x))

def f1(s):
	l = s.split("\n")
	res = 0
	for line in l:
		_, points =  line.split(":")
		win, nb = points.split("|")
		win_l, nb_l = [int(x) for x in win.split()], [int(x) for x in nb.split()]
		power = 0
		for x in nb_l:
			if x in win_l:
				power += 1
		if power > 0:
			res += 2 ** (power - 1)
	return res

def f2(s):
	l = s.split("\n")
	scratch = [1 for x in l]
	cur = 0
	res = 0
	for line in l:
		_, points =  line.split(":")
		win, nb = points.split("|")
		win_l, nb_l = [int(x) for x in win.split()], [int(x) for x in nb.split()]
		match = 0
		for x in nb_l:
			if x in win_l:
				match += 1
		for i in range(cur + 1, min(len(l), cur + 1 + match)):
			scratch[i] += scratch[cur]
		cur += 1
	return sum(scratch)

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=4, year=2023).strip()
	open("in", "w").write(indata)

if exdata:
	print("ex1:", f1(exdata))
# print("in1:", (in1 := f1(indata)))
if exdata:
	print("ex2:", f2(exdata))
print("in2:", (in2 := f2(indata)))

part = input("Submit? (a/b) | ")
if part == "a" or part == "b":
	__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=4, year=2023)
