from helpers import prepare_some_data, red, green, yellow 



def bigger(a, b):
	return a if a >= b else b

def extend_data(data, lst, p='index1'):
	for j in range(len(lst)):
		if lst[j] not in data.keys():
			data[lst[j]] = {
				'index1': [],
				'index2': []
			}
		data[lst[j]][p].append(j)

def check(data, value):
	obj = data[value]
	if len(obj['index1']) > 0 and len(obj['index2']) > 0:
		return green(value)
	elif len(obj['index1']) > 0:
		return red(value)
	else:
		return yellow(value)


if __name__ == '__main__':
	
	d1 = prepare_some_data(1, 25, 12)
	d2 = prepare_some_data(1, 25, 4)

	data = {}
	extend_data(data, d1)
	extend_data(data, d2, 'index2')

	print(red('only left'))
	print(yellow('only right'))
	print(green('both'))

	print()
	print('{:16}{:16}'.format('File1:', 'File2:'))
	for j in range(bigger(len(d1), len(d2))):
		try:
			f1 = check(data, d1[j])
		except IndexError:
			f1 = ''

		try:
			f2 = check(data, d2[j])
		except IndexError:
			f2 = ''

		# padding issue
		padding_space = 25 - len(f1) if f1 else 25 - len(red(''))
		print(f1, ' ' * padding_space, f2)

