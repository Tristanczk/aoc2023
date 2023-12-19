from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, count, groupby, permutations, product
import math
import re
from sortedcontainers import SortedDict, SortedList, SortedDict
from collections import Counter
import argparse
import numpy as np
from functools import lru_cache

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

letters = {'x': 0, 'm': 1, 'a': 2, 's': 3}

def get_result(wf, vals):
	i = 0
	block = "in"
	while True:
		rule = wf[block][i]
		if i == len(wf[block]) - 1:
			if rule == "A":
				return True
			elif rule == "R":
				return False
			else:
				block = rule
				i = 0
				continue
		condition, dest = rule.split(":")
		letter = condition[0]
		value = int(condition[2:])
		val_letter = vals[letters[letter]]
		if condition[1] == '>':
			if val_letter <= value:
				i += 1
			else:
				if dest == 'R':
					return False
				elif dest == 'A':
					return True
				else:
					block = dest
					i = 0
		else:
			if val_letter >= value:
				i += 1
			else:
				if dest == 'R':
					return False
				elif dest == 'A':
					return True
				else:
					block = dest
					i = 0

def f1(s):
	workflows, parts = s.split("\n\n")
	wf = {}
	for line in workflows.split("\n"):
		name, rules = line[:-1].split('{')
		wf[name] = rules.split(",")
	res = 0
	for part in parts.split("\n"):
		vals = lrint(part)
		if get_result(wf, vals):
			res += sum(vals)
	return res

def f2(s):
	workflows, parts = s.split("\n\n")
	wf = {}
	for line in workflows.split("\n"):
		name, rules = line[:-1].split('{')
		wf[name] = rules.split(",")

	@lru_cache(None)
	def recursion(ranges, node, pos):
		final_ranges = []
		if node == 'R':
			return []
		elif node == 'A':
			return [ranges]
		else:
			ranges = list(ranges)
			rule = wf[node][pos]
			if pos == len(wf[node]) - 1:
				final_ranges.extend(recursion(tuple(ranges), rule, 0))
			else:	
				condition, dest = rule.split(":")
				letter = condition[0]
				value = int(condition[2:])
				cur_range = ranges[letters[letter]]
				if condition[1] == '>':
					if cur_range[1] > value:
						new_ranges = ranges.copy()
						ranges[letters[letter]] = (cur_range[0], value)
						new_ranges[letters[letter]] = (value + 1, cur_range[1])
						final_ranges.extend(recursion(tuple(new_ranges), dest, 0))
						final_ranges.extend(recursion(tuple(ranges), node, pos + 1))
				else:
					if cur_range[0] < value:
						new_ranges = ranges.copy()
						new_ranges[letters[letter]] = (cur_range[0], value - 1)
						ranges[letters[letter]] = (value, cur_range[1])
						final_ranges.extend(recursion(tuple(new_ranges), dest, 0))
						final_ranges.extend(recursion(tuple(ranges), node, pos + 1))
		return final_ranges
	
	valid_ranges = recursion(((1,4000), (1,4000), (1, 4000), (1, 4000)), "in", 0)
	res = 0
	for x in valid_ranges:
		prod = 1
		for y in x:
			prod *= y[1] - y[0] + 1
		res += prod
	return res

args = parse_arguments()

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=19, year=2023).strip()
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
		__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=19, year=2023)
