from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, count, groupby, permutations, product
import math
import re
from sortedcontainers import SortedDict, SortedList, SortedDict
from collections import Counter

direction_4 = [(0,1), (0,-1), (1,0), (-1,0)]
direction_8 = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]

rint = lambda x: map(int, re.findall(r"\d+", x))

#note : for program to word, need to slightly modify input to have seeds and number on 2 different lines so that it is same format as other blocks

def convert_to_dist(l, b):
	b = b.split("\n")
	res = [-1 for x in l]
	for line in b[1:]:
		d, s, r = map(int, line.split())
		for i, v in enumerate(l):
			if res[i] != -1:
				continue
			if v >= s and v < s + r:
				res[i] = d + v - s
	for i in range(len(res)):
		if res[i] == -1:
			res[i] = l[i]
	return res

def convert_to_dist_improved(l, b):
	b = b.split("\n")
	transformed = []
	for line in b[1:]:
		dest, src, r = map(int, line.split())
		nl = []
		# print(f"l: {l}")
		while l:
			elem = l.pop()
			start, end = elem[0], elem[1]
			before = [start, min(end, src)]
			inter = [max(start, src), min(end, src + r)]
			after = [max(src + r, start), end]
			# print(f"before: {before}, inter: {inter}, after: {after}")
			if before[1] > before[0]:
				nl.append(before)
			if inter[1] > inter[0]:
				inter_dest = [inter[0] + dest - src, inter[1] + dest - src]
				transformed.append(inter_dest)
			if after[1] > after[0]:
				nl.append(after)
		l = nl
		# print(f"transformed: {transformed}")
	return transformed + l

def f1(s):
	blocks = s. split("\n\n")
	seeds = blocks[0].split("\n")[1]
	seeds = [int(x) for x in seeds.split()]
	for i in range(1, len(blocks)):
		seeds = convert_to_dist(seeds, blocks[i])
	return min(seeds)


def f2(s):
	blocks = s. split("\n\n")
	seeds = blocks[0].split("\n")[1]
	seeds = seeds.split()
	res = []
	for i in range(0, len(seeds), 2):
		res.append([int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])])
	# print(res)
	for a in range(1, len(blocks)):
		res = convert_to_dist_improved(res, blocks[a])
	ret = float('inf')
	for x in res:
		ret = min(x[0], ret)
	return ret


exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=5, year=2023).strip()
	open("in", "w").write(indata)

if exdata:
	print("ex1:", f1(exdata))
print("in1:", (in1 := f1(indata)))
if exdata:
	print("ex2:", f2(exdata))
print("in2:", (in2 := f2(indata)))

part = input("Submit? (a/b) | ")
if part == "a" or part == "b":
	__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=5, year=2023)
