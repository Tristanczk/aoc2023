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
	res = 0
	for l in s.split("\n"):
		cur = 0
		first, last = -1, -1
		for c in l:
			if c.isdigit():
				if first == -1:
					first = int(c)
				last = int(c)
		res += first * 10 + last
	return res

def getnumber(s):
	if len(s) >= 3:
		if s[:3] == "one":
			return 1
		if s[:3] == "two":
			return 2
		if s[:3] == "six":
			return 6
	if len(s) >= 5:
		if s[:5] == "three":
			return 3
		if s[:5] == "seven":
			return 7
		if s[:5] == "eight":
			return 8
	if len(s) >= 4:
		if s[:4] == "four":
			return 4
		if s[:4] == "five":
			return 5
		if s[:4] == "nine":
			return 9
	return -1
		
		

def f2(s):
	res = 0
	for l in s.split("\n"):
		cur = 0
		first, last = -1, -1
		for i, c in enumerate(l):
			if c.isdigit():
				if first == -1:
					first = int(c)
				last = int(c)
			else:
				if getnumber(l[i:]) != -1:
					if first == -1:
						first = getnumber(l[i:])
					last = getnumber(l[i:])
		res += first * 10 + last
	return res

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=1, year=2023).strip()
	open("in", "w").write(indata)

# if exdata:
# 	print("ex1:", f1(exdata))
# print("in1:", (in1 := f1(indata)))
if exdata:
	print("ex2:", f2(exdata))
print("in2:", (in2 := f2(indata)))

part = input("Submit? (a/b) | ")
if part == "a" or part == "b":
	__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=1, year=2023)
