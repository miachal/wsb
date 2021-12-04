import random

def prepare_some_data(min, max, num):
	return [random.randrange(min, max+1) for i in range(num)]

def red(txt):
	return '\x1b[1;31m{}\x1b[0m'.format(txt)

def green(txt):
	return '\x1b[1;32m{}\x1b[0m'.format(txt)

def yellow(txt):
	return '\x1b[1;33m{}\x1b[0m'.format(txt)
