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
	time, distance = lrint(l[0]), lrint(l[1])
	res = []
	for i in range(len(time)):
		cur = 0
		for j in range(time[i] + 1):
			if j * (time[i] - j) > distance[i]:
				cur += 1
		res.append(cur)
	ret = 1
	for x in res:
		ret *= x
	return ret

def f2(s):
	time = 40709879
	distance = 215105121471005
	cur = 0
	for i in range(time + 1):
		if i * (time - i) > distance:
			cur = time - i + 1 - i
			break
	return cur

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=6, year=2023).strip()
	open("in", "w").write(indata)

if exdata:
	print("ex1:", f1(exdata))
print("in1:", (in1 := f1(indata)))
if exdata:
	print("ex2:", f2(exdata))
print("in2:", (in2 := f2(indata)))

part = input("Submit? (a/b) | ")
if part == "a" or part == "b":
	__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=6, year=2023)
