import unittest
from coder import Coder


class CoderTests(unittest.TestCase):
	def test_instance(self):
		coder = Coder()
		self.assertIsInstance(coder, Coder)

	def test_dec2bin(self):
		coder = Coder()
		expectations = [
			[4, '100'],
			[1, '1'],
			[0, '0']
		]
		for dec, bin in expectations:
			self.assertEqual(coder.dec2bin(dec), bin)

	def test_bin2ascii(self):
		coder = Coder()
		expectations = [
			['1000001', 'A'],
			['0001000001', 'A'],
			['1000010', 'B'],
		]
		for bits, ascii in expectations:
			self.assertEqual(coder.bits2ascii(bits), ascii)

	def test_extend(self):
		coder = Coder()
		expectations = [
			[('0', 8), '00000000'],
			[('111', 5), '00111'],
			[('101', 8), '00000101'],
			[('011', 4), '0011']
		]
		for inp, res in expectations:
			num, bits = inp
			self.assertEqual(coder.extend(num, bits), res)

	def test_calc_bits(self):
		coder = Coder()
		expectations = [
			[4, 3], [63, 6], [64, 7], [127, 7],
			[128, 8], [255, 8], [256, 9], [511, 9]
		]
		for num, bits in expectations:
			self.assertEqual(coder.calc_bits(num), bits)

	def test_find_max(self):
		coder = Coder()
		expectations = [
			[[1,2,3,4,5,6,7,8], 4],
			[[1,2,3], 2],
			[[13, 63, 128], 8]
		]
		for arr, max in expectations:
			self.assertEqual(coder.find_max(arr), max)

	def test_calc_redundant(self):
		coder = Coder()
		expectations = [
			[63, 1],
			[3, 5],
			[1, 7],
			[9, 7]
		]
		for a, b in expectations:
			self.assertEqual(coder.calc_redundant(a), b)

	def test_count_bits(self):
		coder = Coder()
		expectations = [
			['10000001', [1, 6, 1]],
			['00000001', [7, 1]],
			['00000000', [8]],
			['11001101', [2, 2, 2, 1, 1]],
			['11110001', [4, 3, 1]]
		]
		for bits, sequence in expectations:
			self.assertEqual(coder.count_bits(bits), sequence)

	def test_split_big_num(self):
		coder = Coder()
		expectations = [
			[700, [255, 0, 255, 0, 190]],
			[500, [255, 0, 245]],
			[255, 255],
			[10, 10],
			[256, [255, 0, 1]]
		]
		for num, sequence in expectations:
			self.assertEqual(coder.split_big_num(num), sequence)

	def test_split_sequence(self):
		coder = Coder()
		expectations = [
			[[500, 20, 10, 700, 25], [255, 0, 245, 20, 10, 255, 0, 255, 0, 190, 25]],
			[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
		]
		for full, splitted in expectations:
			self.assertEqual(coder.split_sequence(full), splitted)

	def test_code(self):
		coder = Coder()
		text = '!AB*'
		expected = '00000011011001100010101010100001001001001001001001001000'
		self.assertEqual(coder.code(text), expected)

	def test_code_as_ascii(self):
		coder = Coder()
		text = '!AB*'
		expected = '\x03f*¡$\x92H'
		self.assertEqual(coder.code_as_ascii(text), expected)
	

if __name__ == '__main__':
	unittest.main()