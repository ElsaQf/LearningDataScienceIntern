#!/usr/bin python

import sys

def func_mapper():
	for line in sys.stdin:
		line = line.strip()
		words = line.split()
		for word in words:
			print '%s\t%s' % (word, 1)
	return 0

if __name__ == '__main__':
	func_mapper()

