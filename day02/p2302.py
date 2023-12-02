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
		game, cubes = line.split(":")
		_, id = game.split(" ")
		valid = True
		for draw in cubes.split(";"):
			d = defaultdict(int)
			for val in draw.split(","):
				n, col = val.strip().split(" ")
				d[col] += int(n)
			if d["red"] > 12 or d["green"] > 13 or d["blue"] > 14:
				valid = False
		if valid:
			res += int(id)
	return res

def f2(s):
	l = s.split("\n")
	res = 0
	for line in l:
		game, cubes = line.split(":")
		_, id = game.split(" ")
		mini = {"red": 0, "blue": 0, "green": 0}
		for draw in cubes.split(";"):
			d = defaultdict(int)
			for val in draw.split(","):
				n, col = val.strip().split(" ")
				d[col] += int(n)
			for color in mini.keys():
				mini[color] = max(mini[color], d[color])
		res += mini["red"] * mini["blue"] * mini["green"]
	return res

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=2, year=2023).strip()
	open("in", "w").write(indata)

if exdata:
	print("ex1:", f1(exdata))
print("in1:", (in1 := f1(indata)))
if exdata:
	print("ex2:", f2(exdata))
print("in2:", (in2 := f2(indata)))

part = input("Submit? (a/b) | ")
if part == "a" or part == "b":
	__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=2, year=2023)
