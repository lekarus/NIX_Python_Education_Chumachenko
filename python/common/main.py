import re


def power3(ls):
	for i in ls:
		yield i ** 3


power = power3([i for i in range(1, 1000)])
print(power)

def capital_decorator(func):
	def wrapper(arg):
		if type(arg) != str:
			func(arg)
			return
		final_str = ''
		sentences = re.split(r'[!?.]', arg)
		counter = 0
		for i, sentence in zip(range(len(sentences)), sentences):
			if sentence == '':
				continue
			counter = counter + len(sentence)
			if i != 0:
				counter += 1
			first_letter = 0
			while sentence[first_letter] == ' ':
				first_letter += 1
			final_str = final_str + sentence[first_letter].upper() + sentence[1+first_letter:].lower() + (arg[counter])
		func(final_str)
	return wrapper

@capital_decorator
def beauty_output(string):
	print(string)

beauty_output('     hELlO, WoRlD!          CIao, MOdO!')

class LettersIterator:
	LETTERS = 'qwertyuiop'
	
	def __init__(self):
		self.counter = -1

	def __iter__(self):
		return self

	def __next__(self):
		self.counter += 1
		if self.counter == len(self.LETTERS):
			raise StopIteration 
		return self.LETTERS[self.counter]

for i in LettersIterator():
	print(i)


class CreaterSequence():
	def __init__(self, number):
		if type(number) != int:
			raise TypeError
		if number <= 1:
			print('need more number')
			raise ValueError
		self.sequence = list(range(1, number))

	def __enter__(self):
		print(f'Start work with sequence {self.sequence}')
		self.sequence.reverse()
		return self

	def print_seq(self):
		print(self.sequence)

	def __exit__(self, type, value, traceback):
		self.sequence.reverse()
		print(f'End work with sequence {self.sequence}')

with CreaterSequence(5) as s:
	s.print_seq()