import os
import sys
import math
from collections import deque

class node:
	def __init__(self):
		self.left = None
		self.right = None
		self.label = None
		self.attr = None
		self.splitval = None

def equalx(data):
	for i in range(0, len(data) - 1):
		if data[i][0 : al] != data[i + 1][0 : al]:
			return False
	return True

def equaly(data):
	for i in range(0, len(data) - 1):
		if data[i][al] != data[i + 1][al]:
			return False
	return True

def mode(data):
	labels = ['AAA', 'AA', 'A', 'BBB', 'BB', 'B', 'CCC']
	count = dict((k, 0) for k in labels)

	for x in data:
		count[x[al]] += 1

	maxv = 0
	maxl = ''
	for x in labels:
		if count[x] > maxv:
			maxv = count[x]
			maxl = x

	c = 0
	for x in labels:
		if count[x] == maxv:
			if c == 1:
				return 'unknown'
			c += 1
	return maxl

def information(data):
	count = dict((k, 0) for k in labels)
	for x in data:
		count[x[al]] += 1

	result = 0
	for x in labels:
		if count[x] != 0:
			p = float(count[x]) / float(len(data))
			result -= p * math.log(p, 2)
	return result

def split(data, att, val):
	less = list()
	greater = list()
	for x in data:
		if float (x[d[att]]) > val:
			greater.append(x)
		else:
			less.append(x)
	return less, greater

def choose_split(data):
	best_gain = 0
	best_attr = ''
	best_splitval = 0
	for x in range(0, al):
		arr = list()
		for y in data:
			arr.append(float(y[d[attr[x]]]))
		arr.sort()
		for i in range(0, len(arr) - 1):
			splitval = 0.5 * (arr[i] + arr[i + 1])
			less, greater = split(data, attr[x], splitval)
			p1 = float(len(less)) / float(len(data))
			p2 = float(len(greater)) / float(len(data))
			remainder = p1 * information(less) + p2 * information(greater)
			gain = information(data) - remainder
			if gain > best_gain:
				best_gain = gain
				best_attr = attr[x]
				best_splitval = splitval
	return best_attr, best_splitval

def DTL(data, minleaf):
	N = len(data)
	if N <= minleaf or equalx(data) or equaly(data):
		n = node()
		n.label = mode(data)
		return n
	n = node()
	n.attr, n.splitval = choose_split(data)
	le, ri = split(data, n.attr, n.splitval)
	n.left = DTL(le, minleaf)
	n.right = DTL(ri, minleaf)
	return n

def predict(n, data):
	while n.label == None:
		if float(data[d[n.attr]]) > n.splitval:
			n = n.right
		else:
			n = n.left
	return n.label

def main():
	ftrain = sys.argv[1]
	ftest = sys.argv[2]
	ml = int(sys.argv[3])
	fp = open(ftrain)

	global labels

	labels = ['AAA', 'AA', 'A', 'BBB', 'BB', 'B', 'CCC']

	lines = fp.readlines()
	l = len(lines)
	train_set = list() 
	global attr
	attr = lines[0].split( )
	index = 0
	global d
	d = dict((k, 0) for k in attr)

	for a in attr:
		d[a] = index
		index += 1

	for i in range(1, l):
		values = lines[i].split( )
		train_set.append(values)
	global al
	al = len(values) - 1
	fp.close()

	root = DTL(train_set, ml)

	fp = open(ftest)

	lines = fp.readlines()
	l = len(lines)
	test_set = list() 
	index = 0

	for i in range(1, l):
		values = lines[i].split( )
		test_set.append(values)

	fp.close()

	for x in test_set:
		print(predict(root, x))
if __name__ == '__main__':
	main()