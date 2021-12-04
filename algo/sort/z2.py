import random
from z1 import guess_random, guess_with_limitation, guess_with_bisection

def test_algo(algo, max=1000, probes=1):
	no_of_shots = 0
	for j in range(probes):
		num_to_guess = random.randint(1, max+1)
		last_no_of_shots = algo(num_to_guess, max)
		no_of_shots += last_no_of_shots
	return no_of_shots / probes


if __name__ == '__main__':
	no_of_probes = int(1e6)
	print('2.A: random: ', test_algo(guess_random, probes=no_of_probes))
	print('2.B: limitation: ', test_algo(guess_with_limitation, probes=no_of_probes))
	print('2.C: bisection: ', test_algo(guess_with_bisection, probes=no_of_probes))

# 2.A: random:  998.007809
# 2.B: limitation:  12.98403
# 2.C: bisection:  8.989986