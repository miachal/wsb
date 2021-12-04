import random

# 1.A
def guess_random(num, max):
	no_of_shots = 0
	while True:
		shot = random.randint(1, max+1)
		no_of_shots += 1
		if (shot == num):
			break	
	return no_of_shots

# 1.B
def guess_with_limitation(num, max):
	no_of_shots = 0
	min = 1
	while True:
		shot = random.randint(min, max+1)
		no_of_shots += 1
		if shot > num:
			max = shot - 1
		elif shot < num:
			min = shot + 1
		else:
			break
	return no_of_shots

# 1.C
def guess_with_bisection(num, max):
	no_of_shots = 0
	number_list = range(1, max+1)
	left_index = 0
	right_index = len(number_list) - 1
	while left_index <= right_index:
		mid_index = (left_index + right_index) // 2
		no_of_shots +=1
		if number_list[mid_index] > num:
			right_index = mid_index - 1
		elif number_list[mid_index] < num:
			left_index = mid_index + 1
		else:
			break
	return no_of_shots


if __name__ == '__main__':
	num = int(input('Your type [1-1000]: '))
	max = num if num > 1000 else 1000

	print('1.A: Looking for: ', num, ' - shots: ', guess_random(num, max))
	print('1.B: Looking for: ', num, ' - shots: ', guess_with_limitation(num, max))
	print('1.C: Looking for: ', num, ' - shots: ', guess_with_bisection(num, max))