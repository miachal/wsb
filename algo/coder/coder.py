class Coder:
	def dec2bin(self, num):
		result = '' if num != 0 else '0'
		while num >= 1:
			num, rest = divmod(num, 2)
			result += str(rest)
		return ''.join([result[i] for i in range(len(result) -1, -1, -1)])

	def bits2ascii(self, str_bits):
		return chr(int(f'0b{str_bits}', 2))	

	def extend(self, str_num, bits=8):
		diff = bits - len(str_num)
		if diff > 0:
			return '0' * diff + str_num
		return str_num

	def calc_bits(self, num):
		return len(self.dec2bin(num))

	def find_max(self, arr):
		max = 0
		for j in arr:
			bits = self.calc_bits(j)
			if bits > max:
				max = bits
		return max

	def calc_redundant(self, num):
		return 8 - (num % 8)

	def count_bits(self, str_num):
		sequence = []
		last_char = str_num[0] 
		counter = 1
		for j in range(1, len(str_num)):
			if str_num[j] != last_char:
				sequence.append(counter)
				counter = 1
				last_char = str_num[j]
			else:
				counter += 1
			if j == len(str_num) - 1:
				sequence.append(counter)
		return sequence

	def split_big_num(self, num):
		if num < 256:
			return num
		result = []
		num, rest = divmod(num, 255)
		for j in range(num):
			result.append(255)
			result.append(0)
		result.append(rest)
		return result

	def split_sequence(self, sequence):
		seq = []
		for num in sequence:
			splitted = self.split_big_num(num)
			seq.extend(splitted) if isinstance(splitted, list) else seq.append(splitted)
		return seq

	def code(self, text):
		bits = ''.join([self.dec2bin(ord(ch)) for ch in text])
		# print('bits_array: ', bits)
		sequence = self.count_bits(bits)
		# print('sequence: ', sequence)
		max_bits = self.find_max(sequence)
		# print('max bits: ', max_bits)
		bits_sequence = [self.extend(self.dec2bin(ch), max_bits) for ch in sequence]
		# print('bits sequence: ', bits_sequence)
		bits_string = ''.join(bits_sequence)
		# print('bits string: ', bits_string)
		bits_redundant = self.calc_redundant(8 + 3 + len(bits_string))
		# print('redundant: ', bits_redundant)
		message = ''.join([
			self.extend(self.dec2bin(max_bits), 8),
			self.extend(self.dec2bin(bits_redundant), 3),
			bits_string,
			'0' * bits_redundant
		])
		# print('message: ', message)
		return message

	def code_as_ascii(self, text):
		message = self.code(text)
		ascii_message = ''
		arr = ['' for j in range(len(message) // 8)]
		for j in range(len(message)):
			arr[j//8] += message[j]
		for bits in arr:
			ascii_message += self.bits2ascii(bits)
		return ascii_message


if __name__ == '__main__':
	c = Coder()
	msg = c.code('!AB*')
	ascii = c.code_as_ascii('!AB*')

	print('Message: ', msg)
	print('Ascii: ', ascii)
