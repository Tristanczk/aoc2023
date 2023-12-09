from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, count, groupby, permutations, product
import math
import re
from sortedcontainers import SortedDict, SortedList, SortedDict
from collections import Counter
import numpy as np

direction_4 = [(0,1), (0,-1), (1,0), (-1,0)]
direction_8 = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]

rint = lambda x: map(int, re.findall(r"\d+", x))
lrint = lambda x: list(map(int, re.findall(r"\d+", x)))

def f1(s):
	l = s.split("\n")
	inst = l[0]
	d = {}
	for line in l[2:]:
		orig, dest = line.replace(" ", "").split("=")
		l, r = dest[1:-1].split(",")
		d[orig] = (l, r)
	i = 0
	j = 0
	cur = 'AAA'
	while True:
		i += 1
		val = inst[j]
		if val == 'R':
			cur = d[cur][1]
		else:
			cur = d[cur][0]
		if cur == 'ZZZ':
			break
		j += 1
		if j >= len(inst):
			j = 0
	return i

def f2(s):
	l = s.split("\n")
	inst = l[0]
	d = {}
	start = []
	for line in l[2:]:
		orig, dest = line.replace(" ", "").split("=")
		if orig[-1] == 'A':
			start.append(orig)
		l, r = dest[1:-1].split(",")
		d[orig] = (l, r)
	i = 0
	j = 0
	result = []
	for cur in start:
		i = 0
		j = 0
		while True:
			i += 1
			val = inst[j]
			if val == 'R':
				cur = d[cur][1]
			else:
				cur = d[cur][0]
			if cur[-1] == 'Z':
				break
			j += 1
			if j >= len(inst):
				j = 0
		result.append(i)
	# found out by printing that results were cyclic so we can just take the lowest common multiplicator
	return np.lcm.reduce(np.array(result))

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=8, year=2023).strip()
	open("in", "w").write(indata)

if exdata:
	print("ex1:", f1(exdata))
print("in1:", (in1 := f1(indata)))
if exdata:
	print("ex2:", f2(exdata))
print("in2:", (in2 := f2(indata)))

part = input("Submit? (a/b) | ")
if part == "a" or part == "b":
	__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=8, year=2023)
