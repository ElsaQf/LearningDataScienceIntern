#!/usr/bin python

import os
import sys
from operator import itemgetter

word2count = {}

def func_reducer():
	for line in sys.stdin:
		line = line.strip()
		word, count = line.split()
		try:
			count = int(count)
			word2count[word] = word2count.get(word, 0) + count
		except ValueError:
			pass

	word2count_sorted = sorted(word2count.items(), key=itemgetter(0))
	for word, count in word2count_sorted:
		print '%s\t%s' % (word, count)
	return 0

if __name__ == '__main__':
	func_reducer()
	
