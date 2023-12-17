from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, count, groupby, permutations, product
import math
import re
from sortedcontainers import SortedDict, SortedList, SortedDict
from collections import Counter
import argparse
import numpy as np

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

def hash(s):
	res = 0
	for c in s:
		res += ord(c)
		res *= 17
		res %= 256
	return res

def find_label_operation_value(s):
	label = 0
	operation = None
	value = None
	if '=' in s:
		label, val = s.split('=')
		label_val = hash(label)
		return label, label_val, '=', int(val)
	else:
		label_val = hash(s[:-1])
		return s[:-1], label_val, '-', None


def f1(s):
	l = s.split('\n')
	res = 0
	for line in l:
		strings = line.split(',')
		for s in strings:
			res += hash(s)
	return res

def f2(s):
	l = s.split('\n')
	res = 0
	boxes = {x: [] for x in range(256)}
	for line in l:
		strings = line.split(',')
		for s in strings:
			label, box, op, val = find_label_operation_value(s)
			found = False
			if op == '=':
				for i in range(len(boxes[box])):
					if boxes[box][i][0] == label:
						boxes[box][i][1] = val
						found = True
						break
				if not found:
					boxes[box].append([label, val])
			else:
				for i in range(len(boxes[box])):
					if boxes[box][i][0] == label:
						del boxes[box][i]
						break
	for box in boxes:
		cur = 0
		for i, lens in enumerate(boxes[box]):
			cur += (box + 1) * (i + 1) * lens[1]
		res += cur
	return res

args = parse_arguments()

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=15, year=2023).strip()
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
		__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=15, year=2023)
