from main import *


def test_even():
	assert even_odd(0) == 'even'
	assert even_odd(4) == 'even'
	assert even_odd(1) == 'odd'
	assert even_odd(3) == 'even'