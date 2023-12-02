#!/usr/bin/env python

# work on both macos and linux
# post to #competitive_programming

import os
from pathlib import Path
import re
import sys


def get_folder(day):
	assert 1 <= day <= 25
	return f"day{day:02}"


def parse_year():
	cwd = os.getcwd().split("/")[-1]
	if not re.fullmatch(r"aoc\d{4}", cwd):
		return None
	return int(cwd[-4:])


def parse_day():
	if len(sys.argv) != 2:
		print("fail")
		return None
	try:
		day = int(sys.argv[1])
	except ValueError:
		return None
	if day < 1 or day > 25:
		return None
	return None if os.path.exists(get_folder(day)) else day


if (year := parse_year()) is None or (day := parse_day()) is None:
	print("Usage (from aocXXXX directory): aoc <day>")
	sys.exit(1)
folder = get_folder(day)
os.mkdir(folder)
Path(f"{folder}/ex").touch()
Path(f"{folder}/in").touch()
python_file = f"{folder}/p{year%100:02}{day:02}.py"
Path(python_file).touch()
open(python_file, "w").write(
	f"""from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, count, groupby, permutations, product
import math
import re
from sortedcontainers import SortedDict, SortedList, SortedDict
from collections import Counter

direction_4 = [(0,1), (0,-1), (1,0), (-1,0)]
direction_8 = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]

rint = lambda x: map(int, re.findall(r"\d+", x))

def f1(s):
	return

def f2(s):
	return f1(s)

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day={day}, year={year}).strip()
	open("in", "w").write(indata)

if exdata:
	print("ex1:", f1(exdata))
print("in1:", (in1 := f1(indata)))
if exdata:
	print("ex2:", f2(exdata))
print("in2:", (in2 := f2(indata)))

part = input("Submit? (a/b) | ")
if part == "a" or part == "b":
	__import__("aocd").submit(in1 if part == "a" else in2, part=part, day={day}, year={year})
"""
)