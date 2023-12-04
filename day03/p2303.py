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
	l = s.split('\n')
	i = 0
	res = 0
	while i < len(l):
		j = 0
		while j < len(l[i]):
			if l[i][j].isdigit():
				k = j
				while k < len(l[i]) and l[i][k].isdigit():
					k += 1
				number = int(l[i][j:k])
				valid = False
				for x in range(max(0, i - 1), min(i + 2, len(l))):
					for y in range(max(0, j - 1), min(len(l[i]) , k + 1)):
						if l[x][y] != "." and not l[x][y].isdigit():
							valid = True
				if valid:
					res += number
				j = k + 1
			else:
				j += 1
		i += 1
	return res

def f2(s):
	l = s.split('\n')
	i = 0
	res = 0
	n, m = len(l), len(l[0])
	for i in range(n):
		for j in range(m):
			if l[i][j] == '*':
				number = []
				for x in range(max(0, i - 1), min(i + 2, n)):
					y = max(0, j - 1)
					while y < min(j + 2, m):
						if l[x][y].isdigit():
							b, a = y, y
							while b >= 0 and l[x][b].isdigit():
								b -= 1
							while a < m and l[x][a].isdigit():
								a += 1
							val = int(l[x][b + 1:a])
							number.append(val)
							y = a + 1
						else:
							y += 1
				if len(number) == 2:
					res += number[0] * number[1]
	return res
							
						
	return res

exdata = open("ex").read().rstrip()
indata = open("in").read().rstrip()
if not indata:
	indata = __import__("aocd").get_data(day=3, year=2023).strip()
	open("in", "w").write(indata)

if exdata:
	print("ex1:", f1(exdata))
print("in1:", (in1 := f1(indata)))
if exdata:
	print("ex2:", f2(exdata))
print("in2:", (in2 := f2(indata)))

part = input("Submit? (a/b) | ")
if part == "a" or part == "b":
	__import__("aocd").submit(in1 if part == "a" else in2, part=part, day=3, year=2023)
