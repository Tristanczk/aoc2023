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
cards_p1 = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
cards_p2 = {'A': 14, 'K': 13, 'Q': 12, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'J': 1}

def find_level_p1(hand):
	d = defaultdict(int)
	for c in hand:
		d[c] += 1
	l = [value for value in d.values()]
	l.sort(reverse=True)
	level = 0
	if len(l) > 1:
		if l[0] == 2 and l[1] == 1:
			level += 10 ** 10
		elif l[0] == 2 and l[1] == 2:
			level += 10 ** 11
		elif l[0] == 3 and l[1] == 1:
			level += 10 ** 12
		elif l[0] == 3 and l[1] == 2:
			level += 10 ** 13
		elif l[0] == 4 and l[1] == 1:
			level += 10 ** 14
		elif l[0] == 5:
			level += 10 ** 15
	else:
		level += 10 ** 15
	for i, x in enumerate(hand):
		level += cards_p1[x] * 10 ** (8 - 2 * i)
	return level


def find_level_p2(hand):
	d = defaultdict(int)
	for c in hand:
		d[c] += 1
	joker = d['J']
	d['J'] = 0
	l = [value for value in d.values() if value != 0]
	l.sort(reverse=True)
	if len(l) > 0:
		l[0] += joker
	else:
		l.append(5)
	level = 0
	if len(l) > 1:
		if l[0] == 2 and l[1] == 1:
			level += 10 ** 10
		elif l[0] == 2 and l[1] == 2:
			level += 10 ** 11
		elif l[0] == 3 and l[1] == 1:
			level += 10 ** 12
		elif l[0] == 3 and l[1] == 2:
			level += 10 ** 13
		elif l[0] == 4 and l[1] == 1:
			level += 10 ** 14
		elif l[0] == 5:
			level += 10 ** 15
	else:
		level += 10 ** 15
	for i, x in enumerate(hand):
		level += cards_p2[x] * 10 ** (8 - 2 * i)
	return level
	




def f1(s):
	l = s.split("\n")
	res = []
	for line in l:
		hand, bid = line.split()
		level = find_level_p1(hand)
		res.append((level, int(bid)))
	res.sort()
	ret = 0
	for i in range(len(res)):
		_, bid = res[i]
		ret += bid * (i + 1)
	return ret

def f2(s):
	l = s.split("\n")
	res = []
	for line in l:
		hand, bid = line.split()
		level = find_level_p2(hand)
		res.append((level, int(bid)))
	res.sort()
	ret = 0
	for i in range(len(res)):
		_, bid = res[i]
		ret += bid * (i + 1)
	return ret

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=7, year=2023).strip()
	open("in", "w").write(indata)

if exdata:
	print("ex1:", f1(exdata))
print("in1:", (in1 := f1(indata)))
if exdata:
	print("ex2:", f2(exdata))
print("in2:", (in2 := f2(indata)))

part = input("Submit? (a/b) | ")
if part == "a" or part == "b":
	__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=7, year=2023)
