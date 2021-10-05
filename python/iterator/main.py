import re

class MultipleSentencesError(Exception):
	pass


class Sentence:

	def __init__(self, string):
		if type(string) != str:
			raise TypeError
		if len(re.findall(r'[.]{3}|[.;?!]', string)) > 1:
			raise MultipleSentencesError
		if type(re.search(r'[.;?!]', string)) == type(None):
			raise ValueError
		
		self.init_str = string

	@property
	def words(self):
		res = list()
		for i in SentenceIterator(self.init_str):
			res.append(i)
		return res

	@property
	def other_chars(self):
		return re.findall(r'[,./!? ;]', self.init_str)

	def	_words(self):
		return SentenceIterator(self.init_str)

	def __iter__(self):
		return SentenceIterator(self.init_str)

	def __repr__(self):
		chars = re.findall(r'[.,/;:!?"\|@# ]', self.init_str)
		words = re.split(' ', self.init_str)
		return f'<Sentence(words={len(words)}, other_chars={len(chars)})>'

	def __getitem__(self, other):
		return self.words[other]



class SentenceIterator():
	def __init__(self, string):
		self.init_str = string
		self.counter = 0

	def __next__(self):
		tmp_counter = 0
		start = 0
		if self.counter == len(re.split(' ', self.init_str))-1:
			self.counter += 1
			return self.init_str[self.init_str.rindex(' ')+1:-1]
		for i, s in zip(range(len(self.init_str)), self.init_str):
			if s == ' ':
				word = ''
				if tmp_counter == self.counter:
					self.counter += 1
					word = self.init_str[start:(i if self.init_str[i-1] != ',' else i - 1)]
					start = i + 1
					return word
				else:
					tmp_counter += 1
					start = i + 1
		raise StopIteration


	def __iter__(self):
		return self

s = Sentence('Hello, world!')
print(s)
print(s._words())
print(next(s._words()))
print(s.words)
print(s.other_chars)
for word in s:
	print(word)
print(s[1])
print(s[:1])